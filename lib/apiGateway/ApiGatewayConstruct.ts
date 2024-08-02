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

        const schoolResource = api.root.addResource('schools');
        schoolResource.addMethod('Get', new LambdaIntegration(lambdas.schoolLambdaContructs.getAllSchoolsLambda));
        schoolResource.addMethod('POST', new LambdaIntegration(lambdas.schoolLambdaContructs.createSchoolLambda));

        const singleSchool = schoolResource.addResource('{id}');
        singleSchool.addMethod('GET', new LambdaIntegration(lambdas.schoolLambdaContructs.getSchoolByIdLambda));
        singleSchool.addMethod('PUT', new LambdaIntegration(lambdas.schoolLambdaContructs.updateSchoolByIdLambda));

        const studentsResource = api.root.addResource('students');
        studentsResource.addMethod('Get', new LambdaIntegration(lambdas.studentLambdaContructs.getStudentsBySchoolIdLambda));
        studentsResource.addMethod('POST', new LambdaIntegration(lambdas.studentLambdaContructs.createStudentsLambda));

        const studentResource = api.root.addResource('student');
        studentResource.addMethod('Get', new LambdaIntegration(lambdas.studentLambdaContructs.getStudentByIdLambda));
        studentResource.addMethod('POST', new LambdaIntegration(lambdas.studentLambdaContructs.createStudentLambda));
        studentResource.addMethod('PUT', new LambdaIntegration(lambdas.studentLambdaContructs.updateStudentLambda));
        studentResource.addMethod('DELETE', new LambdaIntegration(lambdas.studentLambdaContructs.deleteStudentLambda));
    }
}