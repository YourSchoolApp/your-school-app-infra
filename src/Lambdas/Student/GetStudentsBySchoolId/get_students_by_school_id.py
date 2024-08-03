import os
import json
import sys
sys.path.append('/opt')

from Services.student_service import StudentService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    student_service = StudentService(tableName)

    school_id = None
    
    query_parameters = event.get('queryStringParameters', {})
    school_id = query_parameters.get('school_id', None)

    if school_id is None:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Need school id'})
        }
    
    try:
        students_response = student_service.get_students_by_school_id(school_id)
        
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': f'Could not get stuednts {e}'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(students_response)
    }