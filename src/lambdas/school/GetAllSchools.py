import os;
import json;

def handler(event, context):
    table = os.environ.get('TABLE_NAME')

    response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'tableName': table,
                'functionName': "getAllSchools"
            })
        }

    return response