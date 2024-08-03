import boto3
import boto3.dynamodb
import boto3.dynamodb.conditions

from Models.student import Student

PARTITION_KEY = "school_id"
SORT_KEY = "student_id"

class StudentService():
    def __init__(self, tableName):
        self.tableName = tableName
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(tableName)

    def create_student(self, student_data, school_id):
        student = Student(student_data, school_id)
        item = student.__dict__

        self.table.put_item(
            Item = item
        )

        return student

    def create_students(self, students_data, school_id):
        students = []

        for student_item in students_data:
            item = Student(student_item, school_id)
            students.append(item)

        for i in range(0, len(students), 25):
            batch = students[i:i + 25]
            with self.table.batch_writer() as batch_writer:
                for student in batch:
                    item = student.__dict__
                    batch_writer.put_item(Item=item)
                    
        return students_data

    def get_student_by_id(self, school_id, student_id):
        response = self.table.get_item(
            Key={
                PARTITION_KEY: school_id,
                SORT_KEY: student_id
            }
        )

        return response.get('Item')

    def get_students_by_school_id(self, school_id):
        response = self.table.query(
            KeyConditionExpression = boto3.dynamodb.conditions.Key(PARTITION_KEY).eq(school_id)
        )
        return response.get('Items')

    def update_student(self, student_data, school_id, student_id):
        update_expression = "set "
        expression_attribute_values = {}
        expression_attribute_names = {}
        
        for key, value in student_data.items():
            update_expression += f"#{key} = :{key}, "
            expression_attribute_values[f":{key}"] = value
            expression_attribute_names[f"#{key}"] = key
            
        update_expression = update_expression.rstrip(", ")
        
        self.table.update_item(
            Key={
                PARTITION_KEY: school_id,
                SORT_KEY: student_id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names
        )

    def delete_student(self, school_id, student_id):
        self.table.delete_item(
            Key={
                PARTITION_KEY: school_id,
                SORT_KEY: student_id
            }
        )
