import { Aws, RemovalPolicy } from "aws-cdk-lib";
import { Attribute, AttributeType, Table } from "aws-cdk-lib/aws-dynamodb";
import { Construct } from "constructs";

export class SchoolsDynamoDbTable extends Table {
    public static readonly TABLE_ID = 'Students';
    public static readonly PARTITION_KEY = 'school_id';
    public static readonly SORT_KEY = 'student_id';

    constructor(scope: Construct) {
        super(scope, SchoolsDynamoDbTable.TABLE_ID, {
            tableName: `${Aws.STACK_NAME}-Students`,
            partitionKey: {
                name: SchoolsDynamoDbTable.PARTITION_KEY,
                type: AttributeType.STRING
            } as Attribute,
            sortKey: {
                name: SchoolsDynamoDbTable.SORT_KEY,
                type: AttributeType.STRING
            } as Attribute
        });
    }
}

export default SchoolsDynamoDbTable;