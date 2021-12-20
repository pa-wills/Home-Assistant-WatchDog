# https://aws.amazon.com/blogs/security/how-to-create-an-aws-iam-policy-to-grant-aws-lambda-access-to-an-amazon-dynamodb-table/
# ISO 8601 defines the representation of datetime data in string format.

import boto3
import datetime
import json
import time

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name="ap-southeast-2")
    table = dynamodb.Table("HomeAssistantHeartBeat")
    dt_string = datetime.datetime.now().isoformat()
    response = table.put_item(
        Item = {
            'ID': '8Faraday',
            'alertMessageSent': 'false',
            'LastDetected': json.dumps(str(dt_string))
        }
    )
    return {
        'statusCode': 200
    }
