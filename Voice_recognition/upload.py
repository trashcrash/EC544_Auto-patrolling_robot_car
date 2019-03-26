import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.mp3', 'rb')
s3.Bucket('YOUR_BUCKET_NAME').put_object(Key='test.mp3', Body=data)
