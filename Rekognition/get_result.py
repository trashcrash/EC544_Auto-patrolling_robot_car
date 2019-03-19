import boto3

client = boto3.client('rekognition')

response = client.get_label_detection(
    JobId='Your_Job_Id',
)

print(response, file=open("result.json", "a"))