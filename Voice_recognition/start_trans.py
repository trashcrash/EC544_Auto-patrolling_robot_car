import boto3
import json

client = boto3.client('transcribe')

response = client.start_transcription_job(
    TranscriptionJobName='YOUR_JOB_NAME',
    LanguageCode='en-US',
    MediaSampleRateHertz=44100,
    MediaFormat='mp3',
    Media={
        'MediaFileUri': 'https://s3-us-east-1.amazonaws.com/YOUR_BUCKET/test.mp3'
    }
)

print(response)

