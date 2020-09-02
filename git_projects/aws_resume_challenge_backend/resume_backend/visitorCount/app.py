##
##aws SDK for python
import boto3
from botocore.exceptions import ClientError
import os
import json


##
##environment variables
TABLE_NAME = os.environ['DYNAMO_TABLE']
region = os.environ['REGION_NAME']


def lambda_handler(event, context):
    
    table = boto3.resource("dynamodb", region_name=region).Table(TABLE_NAME)
    try:
        table.put_item(
            Item={
                "webPage":"mainPage",
                'visits':0,
            },
            ConditionExpression='attribute_not_exists(visits)'
        )
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise
    
    try:
        response = table.get_item(
            Key={
                "webPage":"mainPage",
            }
            )

    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'statusCode': 400, 'body': e.response['Error']['Message']}
    
    else:
        item = response['Item']
        table.update_item(
            Key={
                "webPage":"mainPage",
            },
            UpdateExpression='SET visits = :val1',
            ExpressionAttributeValues={
                ':val1': item['visits'] + 1
            }
        )
        
        return {
            "statusCode": 200,
            "headers": { "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({
                "message": float(item['visits'] + 1),
                # "location": ip.text.replace("\n", "")
            }),
        }
