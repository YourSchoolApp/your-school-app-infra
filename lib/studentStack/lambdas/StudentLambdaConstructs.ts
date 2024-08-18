import { Table } from "aws-cdk-lib/aws-dynamodb";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { PythonSharedLayer } from "../../PythonSharedLayer";
import { GetStudentByIdLambda } from "./GetStudentById";
import { GetStudentsBySchoolIdLambda } from "./GetStudentsBySchoolIdLambda";
import { CreateStudentLambda } from "./CreateStudentLambda";
import { CreateStudentsLambda } from "./CreateStudentsLambda";
import { UpdateStudentLambda } from "./UpdateStudentLambda";
import { DeleteStudentLambda } from "./DeleteStudentLambda";

export class StudentLambdaConstruct extends Construct {
    public static readonly ID = 'Student';

    public readonly getStudentByIdLambda: IFunction;
    public readonly getStudentsBySchoolIdLambda: IFunction;
    public readonly createStudentLambda: IFunction;
    public readonly createStudentsLambda: IFunction;
    public readonly updateStudentLambda: IFunction;
    public readonly deleteStudentLambda: IFunction;

    constructor(scope: Construct, dynamoDbTable: Table, sharedLayer: PythonSharedLayer) {
        super(scope, StudentLambdaConstruct.ID);
        
        this.getStudentByIdLambda = new GetStudentByIdLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.getStudentByIdLambda);

        this.getStudentsBySchoolIdLambda = new GetStudentsBySchoolIdLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.getStudentsBySchoolIdLambda);

        this.createStudentLambda = new CreateStudentLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.createStudentLambda);

        this.createStudentsLambda = new CreateStudentsLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.createStudentsLambda);

        this.updateStudentLambda = new UpdateStudentLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.updateStudentLambda);

        this.deleteStudentLambda = new DeleteStudentLambda(this, dynamoDbTable.tableName, sharedLayer);
        dynamoDbTable.grantReadWriteData(this.deleteStudentLambda);
    }
}