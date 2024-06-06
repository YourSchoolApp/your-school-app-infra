import { Construct } from "constructs";
import { LambdaIntegration, RestApi } from "aws-cdk-lib/aws-apigateway";
import { LambdaConstructs } from "../shared/LambdaConstructs";

export class ApiGatewayConstruct extends Construct {
    public static readonly ID = 'YourSchoolAppGateway';

    constructor(scope: Construct, lambdas: LambdaConstructs) 
    {
        super(scope, ApiGatewayConstruct.ID);
        const api = new RestApi(this, ApiGatewayConstruct.ID, {
            restApiName: 'School Api'
        })

        const usersResource = api.root.addResource('schools');
        usersResource.addMethod('Get', new LambdaIntegration(lambdas.schoolLambdaContructs.getAllSchoolsLambda));   
    }
}