import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { defaultLambdaProps } from "./DefaultLambdaProps";

export class GetSchoolByIdLambda extends Function {
    public static readonly ID = "GetSchoolById";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, GetSchoolByIdLambda.ID, {
            ...defaultLambdaProps,
            handler: "GetSchoolById.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}