import json

from services.textract.Textract import textract_client
from utils.utils import rename_file
from services.s3Client.S3Client import s3_client
from config.config import config_obj

class InsuranceOCR:

    def __init__(self, event=None):
        self._event = event

    def ocr_extract_info(self):
        insurance_front_path = self._event.get_insurance_front_path()
        extracted_text = textract_client.get_analyze_id(
            file_name=insurance_front_path
        )

        json_key = rename_file(insurance_front_path, '.jpg', '.json')
        json_key = rename_file(json_key, '.JPG', '.json')
        json_key = rename_file(json_key, '.png', '.json')
        json_key = rename_file(json_key, '.PNG', '.json')
        json_key = rename_file(json_key, '.jpeg', '.json')
        json_key = rename_file(json_key, '.JPEG', '.json')

        s3_client.put_object(
            Bucket=config_obj.get_bucket_name(),
            Key=json_key,
            Body=json.dumps(extracted_text),
            ContentType="application/json"
        )

        return True
