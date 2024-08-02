import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class GetStudentByIdLambda extends Function {
    public static readonly ID = "GetStudentById";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, GetStudentByIdLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/GetStudentById'),
            handler: "get_student_by_id.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}