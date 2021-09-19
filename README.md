# Home-Assistant-WatchDog
An AWS-powered watchdog that alerts me when HA dies

## Dev Progress
I have managed to:
* Create the DyDB table.
* Create the execution role for the lambdas.

## Test Progess
* Running the stack, then running the heartBeat lambda - works.

## ToDo:
* Obviously the lambdas themselves. Quite probably these need to be compiled separately, and then loaded with CF.
* Would be create to be able to launch this from a command line tool, rather than from the GUI all the time.


https://www.youtube.com/watch?v=P7i01eqmzrs



## Here's a few resources that were helpful
https://www.youtube.com/watch?v=P7i01eqmzrs


https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/
Here's the how-to

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-services-us-west-2.html#w2ab1c35c58c13c15
List of templates.

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
Complete HelloWorld

https://github.com/amazon-archives/serverless-app-examples
Repo of examples

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-permissions.html
Perhaps these are the perms I need. Set up a new user with these.

# Progress
Attack the HellowWorld example.

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html

I suspect that it is defaulting to an invalid S3 bucket name. I should specify it, to eliminate the error.

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html

interesting walk-through

PErhaps try creating the bucket explicitly, and go from there.
No difference

https://lumigo.io/aws-lambda-deployment/aws-lambda-cloudformation/
ANother interesting walkthrough.

https://iamondemand.com/blog/how-to-deploy-your-lambda-functions-with-cloudformation/
One more.

https://aws.amazon.com/cloudformation/resources/templates/ap-southeast-2/
Maybe let's just try to get one of these working from the CForm Comsole

DynamoDB_Table.template - looks innocuous
..... and it works. So, that's something. Perhaps I can work on a definition that 

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html

The example I keep returning to
https://www.youtube.com/watch?v=P7i01eqmzrs&t=1508s
https://github.com/aws-samples/aws-serverless-samfarm


