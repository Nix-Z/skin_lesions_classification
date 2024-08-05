import os
import boto3

def load_data():
    s3 = boto3.client('s3')
    bucket_name = 'usecases-data'
    url = s3.generate_presigned_url(
                    ClientMethod='get_object',
                    Params={'Bucket': bucket_name, 'Key': 'lesions_image_data.zip'},
                    ExpiresIn=7200  # URL expiration time in seconds (adjust as needed)
                )
    print(url)
    return url

load_data()
