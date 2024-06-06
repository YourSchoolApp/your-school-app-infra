import * as lambda from 'aws-cdk-lib/aws-lambda';

export const defaultLambdaProps : DefaultLambdaProps = {
    runtime: lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset('./src/lambdas/school'),
}

export interface DefaultLambdaProps {
    runtime: lambda.Runtime,
    code: lambda.Code
}