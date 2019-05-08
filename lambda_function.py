import boto3
import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Got Event:')
    logger.info(json.dumps(event))
    custom_tags = [        
        {
            'Key': 'BU',
            'Value': 'IT'
        }
    ]
    ec2resource = boto3.resource('ec2', event['detail']['awsRegion'])
    bolt = ec2resource.Instance(event['detail']['responseElements']['instancesSet']['items'][0]['instanceId'])
    logger.info('attempting to add custom tags {} to instanceid {} in {}'.format(custom_tags, event['detail']['responseElements']['instancesSet']['items'][0]['instanceId'], event['detail']['awsRegion']))
    try:
        bolt.create_tags(Tags=custom_tags)
    except:
        logger.info('an error occured')
        return {
            'statusCode': 400,
            'body': json.dumps('an error occured')
        }
    return {
            'statusCode': 200
    }
    logger.info('success')