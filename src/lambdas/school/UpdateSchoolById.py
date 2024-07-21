import os
import json
import boto3
from boto3.dynamodb.conditions import Key

from Models.School import School

tableName = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

def lambda_handler(event, context):
    
    school_data = event.get('school')
    
    if not school_data or 'id' not in school_data:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'school data with id is required'})
        }
    
    school = School(school_data, school_data['id'])
    
    try:
        update_expression = "SET schoolName = :schoolName, registrationNo = :registrationNo, registeredTo = :registeredTo, address = :address, phoneNos = :phoneNos, pocName = :pocName, pocNos = :pocNos, emails = :emails"
        expression_attribute_values = {
            ':schoolName': school.schoolName,
            ':registrationNo': school.registrationNo,
            ':registeredTo': school.registeredTo,
            ':address': school.address,
            ':phoneNos': school.phoneNos,
            ':pocName': school.pocName,
            ':pocNos': school.pocNos,
            ':emails': school.emails
        }
        
        table.update_item(
            Key={'id': school.id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'School updated successfully'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }
