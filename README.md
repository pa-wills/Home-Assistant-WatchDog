# Home-Assistant-WatchDog
An AWS-powered watchdog that alerts me when HA dies

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



https://aws.amazon.com/cloudformation/resources/templates/ap-southeast-2/
Maybe let's just try to get one of these working from the CForm Comsole

DynamoDB_Table.template - looks innocuous
..... and it works. So, that's something. Perhaps I can work on a definition that 


