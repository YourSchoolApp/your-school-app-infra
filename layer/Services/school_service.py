import boto3

from Models.school import School

class SchoolService:
    def __init__(self, tableName):
        self.tableName = tableName
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(tableName)
        
    def get_all_schools(self):
        schools = []
        response = self.table.scan()
        items = response['Items']
        
        schools = [School(item, item['id']) for item in items]
        return schools
    
    def create_school(self, school_data):
        school = School(school_data)
        item = vars(school)
        self.table.put_item(Item=item)
        
        return school

    def get_school_by_id(self, id):
        response = self.table.get_item(Key={'id': id})
        item = response.get('Item')
        return item
    
    def update_school(self, school_data, id):
        update_expression = "set "
        expression_attribute_values = {}
        expression_attribute_names = {}
        
        for key, value in school_data.items():
            update_expression += f"#{key} = :{key}, "
            expression_attribute_values[f":{key}"] = value
            expression_attribute_names[f"#{key}"] = key
            
        update_expression = update_expression.rstrip(", ")
        
        self.table.update_item(
            Key={
                'id': id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names
        )