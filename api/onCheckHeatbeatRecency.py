import boto3
import json
import datetime
import time

def lambda_handler(event, context):
    notificationThresoldDurationSecs = 5 * 60

    client = boto3.client("sns")
    arnTopic = (client.list_topics())["Topics"][0]["TopicArn"]

    # Compute duration since last poll.
    now = datetime.datetime.now()
    dynamodb = boto3.resource('dynamodb', region_name="ap-southeast-2")
    table = dynamodb.Table("HomeAssistantHeartBeat")
    response = table.get_item(
        Key = {'ID': '8Faraday'}
    )
    thenStr = str(response['Item']['LastDetected']).strip("\"")
    then = datetime.datetime.fromisoformat(thenStr)
    deltaSecs = (now - then).total_seconds()
    
    # If duration > desired, send notification.
    notify = False
    if (deltaSecs > notificationThresoldDurationSecs):
        notify = True
        # TODO notification
        client.publish(TopicArn = arnTopic, Message = "No heartbeat from 8 Faraday for > 5 minutes")

        # TODO set flag and put item
    
    return {
        # TODO: clean up.
        'statusCode': 200,
        'now': json.dumps(str(now)),
        'then': json.dumps(str(response['Item']['LastDetected'])),
        'delta': json.dumps(str(deltaSecs)),
        'notify': json.dumps(str(notify))

    }
