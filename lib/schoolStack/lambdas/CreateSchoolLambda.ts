import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class CreateSchoolLambda extends Function {
    public static readonly ID = "CreateSchool";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, CreateSchoolLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/School/CreateSchool'),
            handler: "create_school.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}