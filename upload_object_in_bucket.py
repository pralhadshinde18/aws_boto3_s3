import logging
import boto3
from botocore.exceptions import ClientError
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logger.error(e)
        return False
    return True


file_name = '/home/pralhad/Documents/git.txt'
bucket_name = 'my-bucket-955295'
object_name = 'gitfiledata'

if upload_file(file_name, bucket_name, object_name):
    logger.info(f"File {file_name} uploaded to {bucket_name} as {object_name}.")
else:
    logger.error(f"Failed to upload {file_name} to {bucket_name}.")



