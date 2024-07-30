import os
import json
import sys
sys.path.append('/opt')

from Services.school_service import SchoolService

tableName = os.environ.get('TABLE_NAME')

def lambda_handler(event, context):
    schoolService = SchoolService(tableName)
    schools = schoolService.get_all_schools()
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps([vars(school) for school in schools])
    }

    return response