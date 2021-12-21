
import boto3
import datetime
import requests
import sys

# TODO: I need to get the URL determination to be a bit smarter. I am going to be screwed if I deploy another APIGW (likely),
# deploy to a different region, etc.
client = boto3.client('apigateway')
response = client.get_rest_apis()
id = response["items"][0]["id"] # ID of the zero'th REST API on this account.
urlHeartbeat = "https://" + id + ".execute-api.ap-southeast-2.amazonaws.com/Prod/heartbeat" # Seems to follow this format.

# TC#01 - invoke the heartbeat API method, and then check the DyDB is correctly populated.
try:
	print("TC #01: Invoke the heartbeat API method, and then check the DyDB is correctly populated.")
	print("Endpoint URL: " + urlHeartbeat)
	r = requests.get(urlHeartbeat)
	dynamodb = boto3.resource('dynamodb', region_name="ap-southeast-2")
	table = dynamodb.Table("HomeAssistantHeartBeat")
	response = table.get_item(
		Key = {'ID': '8Faraday'}
	)
	thenStr = str(response['Item']['LastDetected']).strip("\"")
	then = datetime.datetime.fromisoformat(thenStr)
	deltaSecs = (datetime.datetime.utcnow() - then).total_seconds()
	if (deltaSecs > 5): 
		raise Exception("Heartbeat datetime not reflected in DB.")
	print("TC #01: Passed.")

except:
	print("TC #01: Failed.")
	sys.exit(-1)

sys.exit(0)


