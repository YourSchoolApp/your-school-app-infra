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

        const schoolResource = api.root.addResource('school');
        schoolResource.addMethod('Get', new LambdaIntegration(lambdas.schoolLambdaContructs.getAllSchoolsLambda));
        schoolResource.addMethod('POST', new LambdaIntegration(lambdas.schoolLambdaContructs.createSchoolLambda));

        const singleSchool = schoolResource.addResource('{id}'); // school/{id}
        singleSchool.addMethod('GET', new LambdaIntegration(lambdas.schoolLambdaContructs.getAllSchoolsLambda)); // GET /school/{id}
        singleSchool.addMethod('PUT', new LambdaIntegration(lambdas.schoolLambdaContructs.updateSchoolByIdLambda)); // PUT /school/{id}
    }
}