import boto3

client = boto3.client('sqs', 'us-east-1')
queue_url = client.get_queue_url(
    QueueName='lab6_queue',
)['QueueUrl']

print(queue_url)

response = client.send_message_batch(
    QueueUrl=queue_url,
    Entries=[
        {
            'Id': '1',
            'MessageBody': 'This was message 1'
        },
        {
            'Id': '2',
            'MessageBody': 'This was message 2 with some parameter', 'MessageAttributes': {
                'Parameter': {
                    'StringValue': 'V',
                    'DataType': 'String'
                }
            }
        }
    ]
)

# The “First Received” time for message 1 is 2018-09-25 16:52:17.035 GMT+03:00,
# for message 2 is 2018-09-25 16:52:17.037 GMT+03:00, so there is a slight gap between them.
# The first one had arrived faster.
