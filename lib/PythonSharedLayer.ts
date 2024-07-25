import { Code, LayerVersion, Runtime } from "aws-cdk-lib/aws-lambda";
import { Construct } from 'constructs/lib/construct';

import { resolve } from 'path';

export class PythonSharedLayer extends LayerVersion {
    public static readonly ID = 'PythonSharedLayer';

    constructor(scope: Construct) {
        super(scope, PythonSharedLayer.ID, {
            code: Code.fromAsset(resolve(__dirname, '../layer')),
            compatibleRuntimes: [Runtime.PYTHON_3_9],
            description: 'Python shared modules lambda layer',
        });
    }
}