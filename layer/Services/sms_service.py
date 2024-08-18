from Models.student import Student
from Services.student_service import StudentService
from twilio.rest import Client

class SmsService:
    def __init__(self, account_sid, auth_token, twilio_number, student_table_name):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_number = twilio_number
        self.student_table_name = student_table_name

    def sent_sms(self, message, school_id, student_ids):
        student_service = StudentService(self.student_table_name)
        students_items = student_service.get_students_by_school_id(school_id)
        to_numbers = []

        students = [Student(student_item, school_id, student_item.get('student_id')) for student_item in students_items]
        if student_ids:
            to_numbers = [element['contact_nos'] for element in students if element.get('student_id') in student_ids]

        try:
            client = Client(self.account_sid, self.auth_token)

            for contact_numbers in to_numbers:
                if contact_numbers is not None:
                    primary_number = contact_numbers[0]
                    if not primary_number.startswith('+91'):
                        primary_number = '+91' + primary_number

                    message = client.messages.create(
                        body=message,
                        from_=self.twilio_number,
                        to=primary_number
                    )

        except Exception as e:
            return e