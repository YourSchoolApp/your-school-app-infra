import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class CreateStudentLambda extends Function {
    public static readonly ID = "CreateStudent";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, CreateStudentLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/CreateStudent'),
            handler: "create_student.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}