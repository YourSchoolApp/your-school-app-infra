import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Duration } from "aws-cdk-lib";

export class PostSmsLambda extends Function {
    public static readonly ID = "PostSmsLambda";

    constructor(scope: Construct, studentDbTableName: string, layer: LayerVersion) {
        super(scope, PostSmsLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Sms'),
            handler: "send_sms.lambda_handler",
            timeout: Duration.seconds(900),
            layers: [layer],
            environment: {
                TWILIO_ACCOUNT_SID: 'AC14c8095db87dd519b1a746ccbadcc5a4',
                TWILIO_AUTH_TOKEN: '4f30523bc8bc4887f02373d393f4e32b',
                TWILIO_NUMBER: '+17627635839',
                STUDENT_TABLE_NAME: studentDbTableName
            }
        })
    }
}