import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import SchoolsDynamoDbTable from "./schoolStack/dynamodb/SchoolsDynamoDbTable";
import { SchoolLambdaConstruct } from "./schoolStack/lambdas/SchoolLambdaConstructs";
import { ApiGatewayConstruct } from "./apiGateway/ApiGatewayConstruct";
import { LambdaConstructs } from "./shared/LambdaConstructs";
import StudentDynamoDbTable from "./studentStack/dynamodb/StudentDynamoDbTable";
import { StudentLambdaConstruct } from "./studentStack/lambdas/StudentLambdaConstructs";
import { SmsLambdaConstructs } from "./sms/lambdas/SmsLambdaConstructs";
import { PythonSharedLayer } from "./PythonSharedLayer";

export class YourSchoolAppInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const sharedLayer = new PythonSharedLayer(this);

    const schoolDynamodbTable = new SchoolsDynamoDbTable(this);
    const schoolLambdaConstruct = new SchoolLambdaConstruct(this, schoolDynamodbTable, sharedLayer);

    const studentDynamodbTable = new StudentDynamoDbTable(this);
    const studentLambdaConstruct = new StudentLambdaConstruct(this, studentDynamodbTable, sharedLayer);

    const smsLambdaConstructs = new SmsLambdaConstructs(this, studentDynamodbTable , sharedLayer);

    const lambdaConstructs = new LambdaConstructs();
    lambdaConstructs.schoolLambdaContructs = schoolLambdaConstruct;
    lambdaConstructs.studentLambdaContructs = studentLambdaConstruct;
    lambdaConstructs.smsLambdaConstructs = smsLambdaConstructs;

    new ApiGatewayConstruct(this, lambdaConstructs);
  }
}
