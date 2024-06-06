import os;

def handler(event, context):
    table = os.environ.get('TABLE_NAME')
    response_body = {
        "message": "GetAllSchools from " + table
    }
    return {"statusCode": 200, "body": response_body}