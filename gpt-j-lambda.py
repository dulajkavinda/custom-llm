import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    data = json.loads(json.dumps(event))
    inputPrompt = data['input']
    payload = {"inputs": inputPrompt}

    response = runtime.invoke_endpoint(
                                EndpointName=ENDPOINT_NAME, 
                                ContentType='application/json',
                                Body=json.dumps(payload)
                                )
                                
    result = json.loads(response['Body'].read().decode())
    text = result[0]['generated_text']
    return text