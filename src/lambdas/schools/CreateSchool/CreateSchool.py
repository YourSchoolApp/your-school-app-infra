import os;
import json;
import boto3
import sys

sys.path.append('/opt')
from Models import School

tableName = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    json_input = event['school']
    
    school = School(json_input)
    
    table.put_item(Item=school.to_dict())
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'School object created and inserted into DynamoDB successfully',
            'school': school.to_dict()
        })
    }