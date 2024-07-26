import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class GetAllSchoolsLambda extends Function {
    public static readonly ID = "GetAllSchools";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, GetAllSchoolsLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/lambdas/schools/GetAllSchools'),
            handler: "GetAllSchools.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}