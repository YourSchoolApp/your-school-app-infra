import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class UpdateSchoolByIdLambda extends Function {
    public static readonly ID = "UpdateSchoolById";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, UpdateSchoolByIdLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/lambdas/schools/UpdateSchoolById'),
            handler: "UpdateSchoolById.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}