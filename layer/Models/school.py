import uuid

class School:
    def __init__(self, school_data, school_id=None):
        
        self.school_id = school_id or str(uuid.uuid4())
        self.school_name = school_data.get('school_name')
        self.registration_no = school_data.get('registration_no')
        self.registered_to = school_data.get('registered_to')
        self.address = school_data.get('address')
        self.phone_nos = school_data.get('phone_nos')
        self.poc_name = school_data.get('poc_name')
        self.poc_nos = school_data.get('poc_nos')
        self.emails = school_data.get('emails')

    def __repr__(self):
        
        return (f"School(school_id={self.school_id}, school_name={self.school_name}, "
                f"registration_no={self.registration_no}, registered_to={self.registered_to}, "
                f"address={self.address}, phone_nos={self.phone_nos}, poc_name={self.poc_name}, "
                f"poc_nos={self.poc_nos}, emails={self.emails})")

    def get_school_name(self):
        
        return self.school_name

    def get_contact_info(self):
        
        return {
            'phone_nos': self.phone_nos,
            'poc_name': self.poc_name,
            'poc_nos': self.poc_nos,
            'emails': self.emails
        }