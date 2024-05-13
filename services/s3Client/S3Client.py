import boto3

from config.config import config_obj
class S3Client:

    def __init__(self):
        self._s3_client = boto3.client('s3')
        self._s3_connection = boto3.resource('s3')

    def put_object(self, body, key="", content_type=""):
        self._s3_client.put_object(
            Body=body,
            Bucket=config_obj.get_bucket_name(),
            Key=key,
            ContentType=content_type,
        )
        return True

    def get_object_res(self, file_path=""):
        return self._s3_connection.Object(config_obj.get_bucket_name(), file_path).get()


s3_client = S3Client()