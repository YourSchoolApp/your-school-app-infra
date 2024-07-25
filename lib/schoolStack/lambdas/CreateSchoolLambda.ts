import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

import { defaultLambdaProps } from "./DefaultLambdaProps";

export class CreateSchoolLambda extends Function {
    public static readonly ID = "CreateSchool";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, CreateSchoolLambda.ID, {
            ...defaultLambdaProps,
            handler: "CreateSchool.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}