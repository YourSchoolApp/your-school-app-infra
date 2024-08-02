import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class DeleteStudentLambda extends Function {
    public static readonly ID = "DeleteStudents";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, DeleteStudentLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/DeleteStudent'),
            handler: "delete_student.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}