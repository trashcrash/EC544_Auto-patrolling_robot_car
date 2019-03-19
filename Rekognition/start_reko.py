import boto3

client = boto3.client('rekognition')

response = client.start_label_detection(
    Video={
        'S3Object': {
            'Bucket': 'Your_bucket',
            'Name': 'test.mov'
        }
    },
    NotificationChannel={
        'SNSTopicArn': 'Your_Topic_Arn',
        'RoleArn': 'Your_Role_Arn'
    },
    JobTag='Test1'
)

print(response)