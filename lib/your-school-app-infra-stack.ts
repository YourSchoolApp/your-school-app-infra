import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import SchoolsDynamoDbTable from "./schoolStack/dynamodb/SchoolsDynamoDbTable";
import { SchoolLambdaConstruct } from "./schoolStack/lambdas/SchoolLambdaConstructs";
import { ApiGatewayConstruct } from "./apiGateway/ApiGatewayConstruct";
import { LambdaConstructs } from "./shared/LambdaConstructs";

export class YourSchoolAppInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    //add school stack
    const dynamodbTable = new SchoolsDynamoDbTable(this);
    const schoolLambdaConstruct = new SchoolLambdaConstruct(this, dynamodbTable);

    const lambdaConstructs = new LambdaConstructs();
    lambdaConstructs.schoolLambdaContructs = schoolLambdaConstruct;

    new ApiGatewayConstruct(this, lambdaConstructs);
  }
}
