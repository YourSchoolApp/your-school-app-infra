import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class CreateStudentsLambda extends Function {
    public static readonly ID = "CreateStudents";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, CreateStudentsLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/CreateStudents'),
            handler: "create_students.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}