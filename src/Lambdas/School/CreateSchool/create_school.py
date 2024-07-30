import os
import json
import sys
sys.path.append('/opt')

from Services.school_service import SchoolService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    school_service = SchoolService(tableName)

    request_body = event.get('body')
    
    if request_body is None:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'school info needed in body',
            })
        }
    
    school_data = json.loads(request_body)

    try:
        school = school_service.create_school(school_data)
    except Exception as e:
        return{
            'statusCode': 400,
            'body': json.dumps({'message': 'Could not create school'})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(vars(school))
    }