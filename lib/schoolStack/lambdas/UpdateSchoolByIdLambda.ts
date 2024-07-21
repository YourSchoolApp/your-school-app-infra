import { Function } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { defaultLambdaProps } from "./DefaultLambdaProps";

export class UpdateSchoolByIdLambda extends Function {
    public static readonly ID = "UpdateSchoolById";

    constructor(scope: Construct, dbTableName: string) {
        super(scope, UpdateSchoolByIdLambda.ID, {
            ...defaultLambdaProps,
            handler: "UpdateSchoolById.lambda_handler",
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}