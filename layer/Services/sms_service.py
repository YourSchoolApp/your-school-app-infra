from Models.student import Student
from Services.student_service import StudentService
from twilio.rest import Client

class SmsService:
    def __init__(self, account_sid, auth_token, twilio_number, student_table_name):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_number = twilio_number
        self.student_table_name = student_table_name

    def sent_sms(self, message, school_id, student_ids=None):
        try:
            # Initialize the student service with the provided table name
            student_service = StudentService(self.student_table_name)
            
            # Retrieve students by school_id
            students_items = student_service.get_students_by_school_id(school_id)
            
            # Initialize a list for contact numbers, which can later be modified
            to_numbers = []

            # Convert the student_items into Student objects
            students = [
                Student(student_item, school_id, student_item.get('student_id'))
                for student_item in students_items
            ]

            # If specific student_ids are provided, filter the contact numbers
            if student_ids:
                to_numbers = [
                    element.contact_nos[0] for element in students 
                    if element.student_id in student_ids and element.contact_nos
                ]
            else:
                # If no student_ids are provided, use all contact numbers
                to_numbers = [
                    element.contact_nos[0] for element in students if element.contact_nos
                ]

            # Initialize Twilio client
            client = Client(self.account_sid, self.auth_token)

            # Send messages to each valid contact number
            for contact_number in to_numbers:
                if contact_number:
                    primary_number = contact_number
                    if not primary_number.startswith('+91'):
                        primary_number = '+91' + primary_number

                    # Create and send the message
                    sent_message = client.messages.create(
                        body=message,
                        from_=self.twilio_number,
                        to=primary_number
                    )
                    print(f"Message sent to {primary_number}")

        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return e
