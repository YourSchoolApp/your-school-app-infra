import os
import json
import boto3
import sys

from Models.School import School

sys.path.append('/opt')

tableName = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)
    
def lambda_handler(event, context):
    id = None
    
    path_parameters = event.get('pathParameters', {})
    id = path_parameters.get('id')
    
    if not id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'school_id is required'})
        }
    
    try:
        response = table.get_item(Key={'id': id})
        item = response.get('Item')
        
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'School not found'})
            }
            
        school = School(item, id)
        
        return {
            'statusCode': 200,
            'body': json.dumps(vars(school))
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }