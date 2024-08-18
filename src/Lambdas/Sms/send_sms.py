import json
import os
import sys
sys.path.append('/opt')

from Services.sms_service import SmsService

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
student_table_name = os.environ.get('STUDENT_TABLE_NAME')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body.get('message')
    school_id = None
    student_ids = body.get('student_ids', [])

    query_parameters = event.get('queryStringParameters', {})
    school_id = query_parameters.get('school_id')

    if school_id is None or message is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Need school id and message'})
            }
    
    try: 
        sms_service = SmsService(account_sid, auth_token, twilio_number, student_table_name)
        
        error_message = sms_service.sent_sms(message, school_id, student_ids)

        if error_message is not None:
            return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Could not post sms {error_message}'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Message sent'})
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Could not post sms {e}'})
        }
