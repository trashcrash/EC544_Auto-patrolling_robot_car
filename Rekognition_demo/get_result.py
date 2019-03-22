import boto3

client = boto3.client('rekognition')

response = client.get_label_detection(
    JobId='YourJobId',
)

print(response, file=open("result.json", "a"))
