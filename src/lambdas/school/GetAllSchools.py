import os;
import json;
import boto3

from Models.School import School;

tableName = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    schools = []
    response = table.scan()
    items = response['Items']
    
    schools = [School(item) for item in items]

    response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'schools': [vars(school) for school in schools]
            })
        }

    return response