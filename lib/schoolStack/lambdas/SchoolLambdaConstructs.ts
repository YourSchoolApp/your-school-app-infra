import { Table } from "aws-cdk-lib/aws-dynamodb";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

import { GetAllSchoolsLambda } from "./GetAllSchoolsLambda";
import { CreateSchoolLambda } from "./CreateSchoolLambda";
import { GetSchoolByIdLambda } from "./GetSchoolByIdLambda";
import { UpdateSchoolByIdLambda } from "./UpdateSchoolByIdLambda";
import { PythonSharedLayer } from "../../PythonSharedLayer";

export class SchoolLambdaConstruct extends Construct {
    public static readonly ID = 'SchoolLambdaConstruct';
    public readonly getAllSchoolsLambda: IFunction;
    public readonly createSchoolLambda: IFunction;
    public readonly getSchoolByIdLambda: IFunction;
    public readonly updateSchoolByIdLambda: IFunction;

    constructor(scope: Construct, dynamoDbTable: Table) {
        super(scope, SchoolLambdaConstruct.ID);
        const sharedLayer = new PythonSharedLayer(this);
        
        this.getAllSchoolsLambda = new GetAllSchoolsLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.getAllSchoolsLambda);

        this.createSchoolLambda = new CreateSchoolLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantWriteData(this.createSchoolLambda);

        this.getSchoolByIdLambda = new GetSchoolByIdLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.getSchoolByIdLambda);

        this.updateSchoolByIdLambda = new UpdateSchoolByIdLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantWriteData(this.createSchoolLambda);
    }
}