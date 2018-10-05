import boto3

client = boto3.client('sqs', 'us-east-1')
queue_url = client.get_queue_url(
    QueueName='lab6_queue',
)['QueueUrl']

while True:
    num_max_number_messages = 10
    messages = client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=num_max_number_messages)
    if 'Messages' not in messages.keys():
        print("bye")
        break
    for message in messages['Messages']:
        print(message['Body'])
        response = client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
