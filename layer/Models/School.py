import uuid

class School:
    def __init__(self, schoolData, id = None):
        self.id = id
        if id is None:
            self.id = str(uuid.uuid4())
            
        self.schoolName = schoolData['schoolName']
        self.registrationNo = schoolData['registrationNo']
        self.registeredTo = schoolData['registeredTo']
        self.address = schoolData['address']
        self.phoneNos = schoolData['phoneNos']
        self.pocName = schoolData['pocName']
        self.pocNos = schoolData['pocNos']
        self.emails = schoolData['emails']