# Quick Start Guide: Rubrik Bolt Instance - Custom Tags

## Introduction to Rubrik Bolt Instance - Custom Tags

Many Rubrik customers use cost allocation tags in order to assign cost centers to various assets runninng in their AWS accounts. In order to accomodate such cost allocation methods, the following solution has been created in order to allow for the assignment of custom tags to Rubrik's ephemeral EC2 instnaces.

## Components
The solution consists of the following components:
* An IAM Role, used to execute the lambda function
* An IAM Policy, used to provide the necessary permissions to the IAM Role
* A Lambda function, used to apply custom tags to the Rubrik Bolt instance
* A Cloudwatch event rule, used to trigger the Lambda function when a Rubrik Bolt instance is provisioned 
* A CloudFormation template, used to deploy the above assets into AWS

## Installation
1) Download and package the Lambda function
    * download `lambda_function.py` from this repo
    * edit the `custom_tags` variable in the script as needed. This variable dictates which tags will be applied to bolt when it runs.
    * zip `lambda_function.py` into a zip file named `rubrik_bolt_tag_function.zip`
    * upload `rubrik_bolt_tag.zip` into a S3 bucket located in the region where you wil be deploying this solution
2) Deploy the solution using CloudFormation
    * Create a new stack in your AWS account using `deploy_function_cft.yml`, this template takes the following parameters, all are required:
      * LambdaS3Bucket - Name of the S3 bucket containing your Lambda function zip file - default: none
      * LambdaZipName - Name of the zip file that contains your lambda function - default: rubrik_bolt_tag_function.zip
      * IAMRoleName - Name used for Lambda IAM Role - default: rubrik_bolt_tag_role
      * IAMPolicyName - Name used for Lambda IAM Policy - default: rubrik_bolt_tag_policy
      * CloudWatchEventName - Name used for CloudWatch Event Rule - default: rubrik_bolt_tag_event
      * LambdaFunctionName - Name used for Lambda Function - default: rubrik_bolt_tag_function
3) Verify the solution has successfully deployed
   * The stack should successfully create the Role, Policy, Function, and CloudWatch Event Rule:
![image](https://user-images.githubusercontent.com/16825470/66139399-5bf02800-e5ce-11e9-8c55-8bb991756343.png)
   * Once deployed, new bolt instances should be tagged with the custom tags specified in the `custom_tags` variable
   * Logs for each run will be pushed to a log stream in CloudWatch Logs
