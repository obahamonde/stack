from boto3 import Session
from botocore.exceptions import ClientError
from src.conf import env

aws = Session(
    aws_access_key_id=env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
    region_name=env.AWS_REGION_NAME).client

ses = aws('ses')
s3 = aws('s3')
