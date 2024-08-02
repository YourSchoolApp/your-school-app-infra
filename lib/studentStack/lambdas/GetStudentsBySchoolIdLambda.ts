import { Function, LayerVersion } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class GetStudentsBySchoolIdLambda extends Function {
    public static readonly ID = "GetStudentsBySchoolId";

    constructor(scope: Construct, dbTableName: string, layer: LayerVersion) {
        super(scope, GetStudentsBySchoolIdLambda.ID, {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset('./src/Lambdas/Student/GetStudentsBySchoolId'),
            handler: "get_students_by_school_id.lambda_handler",
            layers: [layer],
            environment: {
                TABLE_NAME: dbTableName
            }
        })
    }
}