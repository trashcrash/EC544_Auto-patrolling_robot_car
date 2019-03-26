import boto3

client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl='Your_sqs_queue_url'
)

print(response)