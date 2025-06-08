import json
import boto3
import os

sns = boto3.client('sns')
topic_arn = os.environ['TOPIC_ARN']

def lambda_handler(event, context):
    for record in event['Records']:
        message_body = record['body']
        try:
            sns.publish(
                TopicArn=topic_arn,
                Message=message_body,
                Subject='New Todo App Action'
            )
            print(f"Published message to SNS: {message_body}")
        except Exception as e:
            print(f"Error publishing to SNS: {e}")
            raise e
    return {
        'statusCode': 200,
        'body': json.dumps('Messages forwarded to SNS')
    }
