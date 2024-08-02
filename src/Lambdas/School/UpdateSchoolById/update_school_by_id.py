import os
import json
import sys
sys.path.append('/opt')

from Services.school_service import SchoolService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    id = None
    
    body = event.get('body')
    path_parameters = event.get('pathParameters', {})
    id = path_parameters.get('id')
    
    if body is None:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'school info needed',
            })
        }
    
    school_service = SchoolService(tableName)
    school_data = json.loads(body)
     
    try:
        school_service.update_school(school_data, id)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item updated successfully'})
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Item not updated {e}'})
        }