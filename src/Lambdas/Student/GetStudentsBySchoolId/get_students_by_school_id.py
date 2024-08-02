import os
import json
import sys
sys.path.append('/opt')

from Services.student_service import StudentService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    student_service = StudentService(tableName)

    school_id = None
    student_id = None
    
    query_parameters = event.get('queryStringParameters', {})
    school_id = query_parameters.get('school_id', None)

    if school_id is None:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Need school id'})
        }
    
    try:
        student = student_service.get_students_by_school_id(school_id, student_id)
        
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Could not create student'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(vars(student))
    }