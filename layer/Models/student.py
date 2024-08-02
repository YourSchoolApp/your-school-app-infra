import uuid

class Student:
    def __init__(self, student_data, school_id, student_id = None):
        
        self.student_id = student_id or str(uuid.uuid4())
        self.school_id = school_id
        self.registration_number = student_data.get('registration_number')
        self.class_roll_number = student_data.get('class_roll_number')
        self.first_name = student_data.get('first_name')
        self.middle_name = student_data.get('middle_name')
        self.last_name = student_data.get('last_name')
        self.dob = student_data.get('dob')
        self.address = student_data.get('address')
        self.contact_nos = student_data.get('contact_nos')
        self.parent_first_name = student_data.get('parent_first_name')
        self.parent_middle_name = student_data.get('parent_middle_name')
        self.parent_last_name = student_data.get('parent_last_name')
        self.gender = student_data.get('gender')
        self.is_active = student_data.get('is_active', True)
        self.last_enrollment_date = student_data.get('last_enrollment_date')
        self.photo_url = student_data.get('photo_url')
        self.student_class = student_data.get('student_class')

    def __repr__(self):
        
        return (f"Student(student_id={self.student_id}, full_name={self.full_name()}, "
                f"student_class={self.student_class})")

    def full_name(self):
        
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def parent_full_name(self):
        
        return f"{self.parent_first_name} {self.parent_middle_name} {self.parent_last_name}"

    def is_active_student(self):
        
        return self.is_active
