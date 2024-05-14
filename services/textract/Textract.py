import boto3

from config.config import config_obj

class Textract:

    def __init__(self):
        self._client = boto3.client('textract')

    def get_analyze_id(self, file_name=""):
        extracted_text = self._client.analyze_id(
            DocumentPages=[{
                "S3Object": {
                    "Bucket": config_obj.get_bucket_name(),
                    "Name": file_name
                }
            }]
        )
        return extracted_text

    def get_multi_analyze_id(self, file_names=[]):
        request = []
        for file_name in file_names:
            request.append({
                "S3Object": {
                    "Bucket": config_obj.get_bucket_name(),
                    "Name": file_name
                }
            })
        extracted_text = self._client.analyze_id(
            DocumentPages=request
        )
        return extracted_text


textract_client = Textract()