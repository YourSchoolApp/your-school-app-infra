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
    
    students_data = json.loads(body)

    try:
        student_service.create_students(students_data)
        
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Could not create students'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Created students"})
    }