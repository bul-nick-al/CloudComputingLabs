import boto3
# create a boto3 client
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
)
# Sending a message to your queue
queue_name = 'lab6_queue'
# Get the queue
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
print(queue_url)