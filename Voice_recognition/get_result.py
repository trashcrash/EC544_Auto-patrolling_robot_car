import boto3
import json

client = boto3.client('transcribe')

response = client.get_transcription_job(
    TranscriptionJobName='YOUR_JOB_NAME'
)
print(response)

