import os
import json
import sys
sys.path.append('/opt')

from Services.student_service import StudentService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    school_id = None
    student_service = StudentService(tableName)

    body = event.get('body')
    
    if body is None:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'school info needed in body',
            })
        }
    
    student_data = json.loads(body)
    query_parameters = event.get('queryStringParameters', {})
    school_id = query_parameters.get('school_id', None)

    if school_id is None:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Need school id in query parameter'})
        }
    
    if school_id is None:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'school info needed in body',
            })
        }

    try:
        student = student_service.create_student(student_data, school_id)
        
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Could not create student'})
        }
    
    return {
        'statusCode': 201,
        'body': json.dumps(student)
    }