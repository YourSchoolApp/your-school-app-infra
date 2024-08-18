import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { PythonSharedLayer } from "../../PythonSharedLayer";
import { PostSmsLambda } from "./PostSmsLambda";
import { Table } from "aws-cdk-lib/aws-dynamodb";

export class SmsLambdaConstructs extends Construct {
    public static readonly ID = 'Sms';

    public readonly postSmsLambda: IFunction;

    constructor(scope: Construct, studentDbTable: Table, sharedLayer: PythonSharedLayer) {
        super(scope, SmsLambdaConstructs.ID);
        
        this.postSmsLambda = new PostSmsLambda(this, studentDbTable.tableName, sharedLayer);
        studentDbTable.grantReadWriteData(this.postSmsLambda);
    }
}