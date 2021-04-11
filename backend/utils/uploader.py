import aiobotocore

from utils.config import settings


async def upload_file(s3_filename, local_file, content_type, public_read=True):
    bucket = settings.s3_upload_bucket

    session = aiobotocore.get_session()
    async with session.create_client(
            "s3",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key
            # endpoint_url=settings.s3_endpoint_url,  # Used for non-AWS S3 compatible storage
    ) as client:
        # Upload object to amazon s3
        await client.put_object(
            Bucket=bucket,
            Key=s3_filename,
            Body=local_file.read(),
            ContentType=content_type,
            ACL="public-read" if public_read else None
        )
        return True
