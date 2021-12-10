# https://aws.amazon.com/blogs/security/how-to-create-an-aws-iam-policy-to-grant-aws-lambda-access-to-an-amazon-dynamodb-table/
# ISO 8601 defines the representation of datetime data in string format.

# TODO: Trigger this from a web-hook exposed through the API GW.
# Purpose: update the tracked time the HA instance last heartbeat'd us.

import boto3
import datetime
import json
import time

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name="ap-southeast-2")
    table = dynamodb.Table("HomeAssistantHeartBeat")
    dt_string = datetime.datetime.now().isoformat()
#    dt_string = time.strftime("%Y-%m-%dT%H:%M:%S%z", time.gmtime())
    response = table.put_item(
        Item = {
            'ID': '8Faraday',
            'alertMessageSent': 'false',
            'LastDetected': json.dumps(str(dt_string))
        }
    )
    
    # TODO: If 'alertMessageSent' was true, send a clearing notification.
    
    return {
        'statusCode': 200
    }
