def handler(event, context):
    response_body = {
        "message": "Testing cdk deployment"
    }
    return {"statusCode": 200, "body": response_body}