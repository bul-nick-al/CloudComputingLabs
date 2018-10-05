import boto3
client = boto3.client('lambda')
response = client.invoke(
    FunctionName='functionLab4',
    Payload=b"""{"param1":"a", "param2":"2", "param3":"4"}""",
)
print(response['Payload'].read())
