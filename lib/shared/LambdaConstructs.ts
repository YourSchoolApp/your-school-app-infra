import { SchoolLambdaConstruct } from "../schoolStack/lambdas/SchoolLambdaConstructs";
import { SmsLambdaConstructs } from "../sms/lambdas/SmsLambdaConstructs";
import { StudentLambdaConstruct } from "../studentStack/lambdas/StudentLambdaConstructs";

export class LambdaConstructs {
    public schoolLambdaContructs : SchoolLambdaConstruct;
    public studentLambdaContructs : StudentLambdaConstruct;
    public smsLambdaConstructs : SmsLambdaConstructs;
}