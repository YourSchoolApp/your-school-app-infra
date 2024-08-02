import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class UpdateStudentLambda extends Function {
    public static readonly ID = "UpdateStudent";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, UpdateStudentLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/UpdateStudent'),
            handler: "update_student.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}