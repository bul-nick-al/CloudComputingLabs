import boto3

client = boto3.client('sqs', 'us-east-1')
# response = client.create_queue(
#     QueueName='lab6_queue',
# )
queues = client.list_queues()
print(queues)
test_queue_url = queues['QueueUrls'][0]
print(test_queue_url)

# B. If I attempt to create another queue, nothing happens, the new queue is not created, as I figured
# from the timestamp in my aws console. An the response contains the information of the already existing queue
# It happens because I attempted to create a queue with the same parameters. If I tried other parameters, it would have
# returned a response with http code 400 and the message QueueAlreadyExists.



x