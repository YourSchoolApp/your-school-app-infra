import { Function } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { defaultLambdaProps } from "./DefaultLambdaProps";

export class GetAllSchoolsLambda extends Function {
    public static readonly ID = "GetAllSchools";

    constructor(scope: Construct, dbTableName: string) {
        super(scope, GetAllSchoolsLambda.ID, {
            ...defaultLambdaProps,
            handler: "GetAllSchools.lambda_handler",
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}