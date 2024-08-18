import os
import json
import sys
sys.path.append('/opt')

from Services.school_service import SchoolService

tableName = os.environ.get('TABLE_NAME')
    
def lambda_handler(event, context):
    id = None
    
    path_parameters = event.get('pathParameters', {})
    school_id = path_parameters.get('id')
    
    try:
        school_service = SchoolService(tableName)
        
        item = school_service.get_school_by_id(school_id)
        
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'School not found'})
            }
            
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }