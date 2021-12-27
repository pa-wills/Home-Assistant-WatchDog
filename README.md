# Home-Assistant-WatchDog
An AWS-powered watchdog that alerts me when my [HomeAssistant](https://www.home-assistant.io/) instance dies.

While this app has some stand-alone utilty - its existence mainly derives from my need for hands-on experience as I attempt to pass the various AWS certs, and as I attempt to improve my practical understanding of CI/CD technology generally. 

Also, while HomeAssistant is the motivating problem, this Watchdog could be extended to any component that's capable of invoking a REST API.

## Contents / Setup
The project comprises two stacks - one for the CI/CD apparatus, and the other for the app itself.
* [pipeline.yaml](pipeline/pipeline.yaml) defines the CI/CD apparatus, which is a distinct stack. To get it working, simply instantiate the template with CloudFormation. Note - you may need to empty and then delete the S3 bucket, prior to running Create, assuming that it exists already (Updates seem to be unaffected / fine). You will also need to authorise the stack to talk to this GitHub repo (go get an OAuth token).
* The application itself is a separate stack, and it should instantiate automatically from the CodePipeline object in the other Stack. It comprises two lambdas, a DyDB table (for state), a SNS topic (for alerting), and some IAM objects.

## How the pipeline works
* Source stage is a simple replication of what's in the GitHub repo (make sure you're on the correct branch!).
* Production stage comprises build, computation of the change set, execution of the change set, and lastly - a smoke test (triggering the heartbeat API, then checking that the state is correctly set in the DyDB table).

![screenshot](https://user-images.githubusercontent.com/34256848/146853028-367306b9-0417-48ea-b9ec-97b22a061f38.png)

## How the app works
* The app presents a basic API for recording heartbeats (see the console / CodeBuild for its URL). 
* Once invoked - the app logs the datetime ([1st lambda](api/onHeartbeatFromHomeAssistant.py)).
* EventBridge then triggers the [2nd lambda](api/onCheckHeartbeatRecency.py) to periodically check the last logged datetime, and notify me if the app has not heartbeat'd recently.
* On the HomeAssistant side (not part of the repo), I have an AppDaemon daemon that invokes the API every _x_ minutes. I give the URL to HomeAssistant statically in the code at the moment (sloppy, I know), but helpfully - AppDaemon detects such changes and restarts automatically. 
* The various waiting periods and notification endpoints - are parameterised into Environment Variables, EventBridge settings. My hope here is that these can thus be modified at runtime (I.e. without the need for a deployment).

## Development off the main branch
Do the following:
* Create a new branch (E.g. dev)
* Create / change the software as you see fit.
* Create the stack using the usual [sam](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html#serverless-sam-cli) commands:

		sam build
		sam package --s3-bucket hawpl-codepl-astore
		sam deploy --s3-bucket hawpl-codepl-astore --stack-name test --capabilities CAPABILITY_NAMED_IAM CAPABILITY_IAM --parameter-overrides EnvironmentType=Dev

* In the above ensure that:
	* Give the stack a disctinct name, like "test"
	* set the Environment Variable _EnvironmentType_ to "Dev". This drives some conditional resource creation, and some distinct resource naming.
* Iterate.
* Merge changes to main. 
* Execute the steps in the prior sections.

## Biggest todos
Obviously see the Issues, but in general:
* Authentication of client to API (or similar).
* Least privilege, generally (the various IAM objects are needlessly permissive).
* More robust ARN inference code, by which I mean: I have written code that goes and fetches the 0'th SNS topic, etc. This works for now, but won't once I build more applications. I need to sandbox those searches to within the app itself.
* It would be nice to add more robust testing to the pipeline.
* Cleanup lambda - so that there's no need for manual activity (see above).
* Client-side API end-point auto-URL-discovery (or something else that would render the URL static).

## Things I found difficult / helpful
* Most notably there's this helpful [sample app](https://github.com/aws-samples/aws-serverless-samfarm), and [video](https://www.youtube.com/watch?v=P7i01eqmzrs&t=1508s). I used this as a guide for designing the app. I especially love their idea of incorporating the pipeline _and_ the app itself as separate stacks within a common repo. This idea is elegant, and I would never have thought to do it.
* Creating the application components individualls in the console turned out to be pretty easy. On reflection the hard part for me was trying to learn CloudFormation, SAM and CodePipeline simulatenously. I probably made that harder for myself by insisting on defining everything statically, bottom-up from the CF template. 

