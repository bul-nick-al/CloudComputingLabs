import boto3


def list_and_create_bucket():
    response = client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    # Print out the bucket list
    print("Bucket List: %s" % buckets)

    if 'my-bucket-lab-4' not in buckets:
        res = client.create_bucket(
            Bucket='my-bucket-lab-4',
            ACL='public-read',
            CreateBucketConfiguration={'LocationConstraint': 'us-east-2'},
        )
        print(res)


def upload_file(filepathname, name):
    client.upload_file(filepathname, 'my-bucket-lab-4', name)


def list_files():
    for key in client.list_objects(Bucket='my-bucket-lab-4')['Contents']:
        print(key['Key'])


def detect_params(filename):
    response = client.detect_labels(Image={'S3Object': {'Bucket': 'my-bucket-lab-4', 'Name': filename}})
    print('\nDetected labels for ' + filename + '\n')
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))


def detect_text(filename):
    response = client.detect_text(Image={'S3Object': {'Bucket': 'my-bucket-lab-4', 'Name': filename}})
    print('\nDetected text for ' + filename + '\n')
    for text in response['TextDetections']:
        print(text['DetectedText'] + ' : ' + str(text['Confidence']))


client = boto3.client('s3')
list_and_create_bucket()
# upload_file('/Users/nicholas/Downloads/sign.jpg', 'sign.jpg')
list_files()
client = boto3.client('rekognition')
detect_params('test.jpg')
detect_text('sign.jpg')



