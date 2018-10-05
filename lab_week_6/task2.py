import boto3

client = boto3.client('sqs', 'us-east-1')
queue_url = client.get_queue_url(
    QueueName='lab6_queue',
)['QueueUrl']

print(queue_url)

response = client.send_message(
    QueueUrl=queue_url,
    MessageBody='this is a message to my queue. Hi!',
)

response = client.receive_message(
    QueueUrl=queue_url,
    MessageAttributeNames=[
        'string',
    ]
)
message = response['Messages'][0]['Body']
print(message)
