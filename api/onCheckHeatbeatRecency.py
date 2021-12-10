import boto3
import json
import datetime
import time

# Something else - is this even necessary. Could I perhaps get CLoudwatch
# to do this for me, and if so - maybe just run SNSS off CWatch.

def lambda_handler(event, context):
    notificationThresoldDurationSecs = 5 * 60

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
        # TODO set flag and put item
    
    return {
        # TODO: clean up.
        'statusCode': 200,
        'now': json.dumps(str(now)),
        'then': json.dumps(str(response['Item']['LastDetected'])),
        'delta': json.dumps(str(deltaSecs)),
        'notify': json.dumps(str(notify))

    }
