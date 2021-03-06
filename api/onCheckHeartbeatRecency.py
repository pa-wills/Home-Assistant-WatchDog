import boto3
import json
import datetime
import os
import time


def lambda_handler(event, context):
    notificationThresoldDurationSecs = int(os.environ.get('NOTIFICATION_WAIT_MINS')) * 60

    client = boto3.client("sns")
    arnTopic = client.create_topic(Name = (str(os.environ.get('APP_NAME')) + "-" + str(os.environ.get('ENV_NAME')) + "-HeartbeatNotificationTopic"))["TopicArn"]

    # Compute duration since last poll.
    now = datetime.datetime.now()
    tableName = str(os.environ.get('APP_NAME')) + "-" + str(os.environ.get('ENV_NAME')) + "-HeartBeatState"
    dynamodb = boto3.resource('dynamodb', region_name = "ap-southeast-2")
    table = dynamodb.Table(tableName)
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
        client.publish(TopicArn = arnTopic, Message = str(os.environ.get('NOTIFICATION_MESSAGE')))
    
    return {
        # TODO: clean up.
        'statusCode': 200,
        'now': json.dumps(str(now)),
        'then': json.dumps(str(response['Item']['LastDetected'])),
        'delta': json.dumps(str(deltaSecs)),
        'notify': json.dumps(str(notify))

    }
