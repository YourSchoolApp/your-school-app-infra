import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class GetSchoolByIdLambda extends Function {
    public static readonly ID = "GetSchoolById";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, GetSchoolByIdLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/School/GetSchoolById'),
            handler: "get_school_by_id.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}