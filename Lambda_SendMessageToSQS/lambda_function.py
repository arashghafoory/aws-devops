import json
import boto3
import os

sqs = boto3.client('sqs')
queue_url = os.environ['SQS_URL']

def lambda_handler(event, context):
    print(event)
    print(context)
    try:
        # Check Body is defined
        if 'body' in event:
            body = event['body']
            if isinstance(body, str):
                data = json.loads(body)
            else:
                data = body
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No body in event'})
            }

        # Process Body Data
        todo_id = data.get('todo_id')
        todo_title = data.get('todo_title')
        todo_action = data.get('todo_action')
      
        # Send Message To SQS
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=f'Todo Application Action Message || #{todo_id}: {todo_title} was {todo_action}'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Processed and sent to SQS'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
