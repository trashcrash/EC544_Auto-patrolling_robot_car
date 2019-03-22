import boto3

client = boto3.client('rekognition')

response = client.start_label_detection(
    Video={
        'S3Object': {
            'Bucket': 'ec544',
            'Name': 'test.mov'
        }
    },
    NotificationChannel={
        'SNSTopicArn': 'YourSNSTopicArn',
        'RoleArn': 'YourRoleArn'
    },
    JobTag='Test1'
)

print(response)
