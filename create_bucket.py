import logging
import boto3
from botocore.exceptions import ClientError

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            # create bucket
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # create bucket with specific region
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logger.error(e)
        return False
    return True


bucket_name = 'pralhadbucket18'
region = 'ap-south-1'
if create_bucket(bucket_name, region):
    logger.info(f"Bucket {bucket_name} created successfully.")
else:
    logger.error(f"Failed to create bucket {bucket_name}.")
