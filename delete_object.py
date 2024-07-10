import boto3
from botocore.exceptions import ClientError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# initialize S3 client
s3_client = boto3.client('s3')


def delete_object(bucket_name, key):
    try:
        response = s3_client.delete_objects(
            Bucket=bucket_name,
            Delete={
                'Objects': [
                    {
                        'Key': key
                    }
                ]
            }
        )
        logger.info(f"Deleted object {key} from bucket {bucket_name}.")
        return response
    except ClientError as e:
        logger.error(e)
        return None


bucket_name = 'my-bucket-955295'
key = 'gitfiledata'

response = delete_object(bucket_name, key)
if response:
    logger.info(f"Response: {response}")
else:
    logger.error("Failed to delete object.")
