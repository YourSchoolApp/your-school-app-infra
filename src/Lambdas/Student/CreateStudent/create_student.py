import os
import json
import sys
sys.path.append('/opt')

from Services.student_service import StudentService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
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

    try:
        student = student_service.create_student(student_data)
        
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Could not create student'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(vars(student))
    }