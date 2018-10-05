import boto3

client = boto3.client('sqs', 'us-east-1')
queue_url = client.get_queue_url(
    QueueName='lab6_queue',
)['QueueUrl']

print(queue_url)

response = client.purge_queue(
    QueueUrl=queue_url
)

print(response)
