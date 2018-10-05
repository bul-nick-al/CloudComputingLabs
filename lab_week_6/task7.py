import boto3

client = boto3.client('sns', 'us-east-1')
response = client.create_topic(
    Name='la6_topic'
)
print('response')

some_list_of_contacts = ['+79127492904', '+79127492904']
for number in some_list_of_contacts:
    client.subscribe(
        TopicArn=response['TopicArn'],
        Protocol='sms',
        Endpoint=number # <-- number who'll receive an SMS message.
)
print(response)

response = client.publish(
    TopicArn=response['TopicArn'],
    Message='Hello world',
)
