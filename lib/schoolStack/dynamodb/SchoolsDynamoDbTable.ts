import { Aws, RemovalPolicy } from "aws-cdk-lib";
import { Attribute, AttributeType, Table } from "aws-cdk-lib/aws-dynamodb";
import { Construct } from "constructs";

export class SchoolsDynamoDbTable extends Table {
    public static readonly TABLE_ID = 'Schools';
    public static readonly PARTITION_KEY = 'id';

    constructor(scope: Construct) {
        super(scope, SchoolsDynamoDbTable.TABLE_ID, {
            tableName: `${Aws.STACK_NAME}-Schools`,
            partitionKey: {
                name: SchoolsDynamoDbTable.PARTITION_KEY,
                type: AttributeType.STRING
            } as Attribute
        });
    }
}

export default SchoolsDynamoDbTable;