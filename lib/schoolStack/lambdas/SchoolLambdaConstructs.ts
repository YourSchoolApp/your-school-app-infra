import { Table } from "aws-cdk-lib/aws-dynamodb";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { GetAllSchoolsLambda } from "./GetAllSchoolsLambda";

export class SchoolLambdaConstruct extends Construct {
    public static readonly ID = 'SchoolLambdaConstruct';
    public readonly getAllSchoolsLambda: IFunction;

    constructor(scope: Construct, dynamoDbTable: Table) {
        super(scope, SchoolLambdaConstruct.ID);
        
        this.getAllSchoolsLambda = new GetAllSchoolsLambda(this, dynamoDbTable.tableName);
        dynamoDbTable.grantReadWriteData(this.getAllSchoolsLambda);
    }
}