import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import SchoolsDynamoDbTable from "./schoolStack/dynamodb/SchoolsDynamoDbTable";
import { SchoolLambdaConstruct } from "./schoolStack/lambdas/SchoolLambdaConstructs";
import { ApiGatewayConstruct } from "./apiGateway/ApiGatewayConstruct";
import { LambdaConstructs } from "./shared/LambdaConstructs";
import StudentDynamoDbTable from "./studentStack/dynamodb/StudentDynamoDbTable";
import { StudentLambdaConstruct } from "./studentStack/lambdas/StudentLambdaConstructs";

export class YourSchoolAppInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    //add school stack
    const schoolDynamodbTable = new SchoolsDynamoDbTable(this);
    const schoolLambdaConstruct = new SchoolLambdaConstruct(this, schoolDynamodbTable);

    const studentDynamodbTable = new StudentDynamoDbTable(this);
    const studentLambdaConstruct = new StudentLambdaConstruct(this, studentDynamodbTable);

    const lambdaConstructs = new LambdaConstructs();
    lambdaConstructs.schoolLambdaContructs = schoolLambdaConstruct;
    lambdaConstructs.studentLambdaContructs = studentLambdaConstruct;

    new ApiGatewayConstruct(this, lambdaConstructs);
  }
}
