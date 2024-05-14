import json
from collections import defaultdict

from services.textract.Textract import textract_client
from utils.utils import rename_file, get_insurance_template
from services.s3Client.S3Client import s3_client

class InsuranceOCR:

    def __init__(self, event=None):
        self._event = event
        self._extracted_info = None
        self._update_exp = ""
        self._exp_attr_name = {}
        self._exp_attr_value = {}
        self._temp_info = defaultdict(str)
        self._insurance_info = get_insurance_template()

    def _populate_generated_data(self, type ="", value_detection =""):
        temp_info = self._temp_info
        if type == "FIRST_NAME":
            temp_info["firstName"] = value_detection
        elif type == "MIDDLE_NAME":
            temp_info["middleName"] = value_detection
        elif type == "LAST_NAME":
            temp_info["lastName"] = value_detection
        elif type == "DATE_OF_BIRTH":
            temp_info["memberDOB"] = value_detection
        elif type == "DOCUMENT_NUMBER":
            temp_info["memberId"] = value_detection

    def generate_query(self):
        temp_info = self._temp_info
        insurance_info = self._insurance_info
        insurance_info["policyHolderName"] = temp_info["firstName"]
        insurance_info["policyHolderName"] += " " + temp_info["middleName"] if temp_info["middleName"].strip() != "" else ""
        insurance_info["policyHolderName"] += " " + temp_info["lastName"] if temp_info["lastName"].strip() != "" else ""
        insurance_info["memberId"] = temp_info["memberId"]

        exp_attr_name = defaultdict(str)
        exp_attr_value = defaultdict(str)
        update_exp_arr = []
        for key, value in insurance_info.items():
            update_exp_arr.append(f"#{key} = :{key}")
            exp_attr_name[f"#{key}"] = key
            exp_attr_value[f":{key}"] = value

        update_exp = "SET " + ", ".join(update_exp_arr)

        return update_exp, exp_attr_name, exp_attr_value



    def extract_fields(self):
        documents = self._extracted_info["IdentityDocuments"] if "IdentityDocuments" in self._extracted_info else []
        for document in documents:
            fields = document["IdentityDocumentFields"] if "IdentityDocumentFields" in document else []
            for field in fields:
                type = field["Type"]["Text"]
                value_detection = field["ValueDetection"]["Text"]
                self._populate_generated_data(type=type, value_detection=value_detection)

    def ocr_extract_info(self):
        self._update_exp = ""
        self._exp_attr_name = {}
        self._exp_attr_value = {}
        self._insurance_info = get_insurance_template()
        self._temp_info = defaultdict(str)
        insurance_front_path = self._event.get_insurance_front_path()
        insurance_back_path = self._event.get_insurance_back_path()
        # extracted_text = textract_client.get_analyze_id(
        #     file_name=insurance_front_path
        # )
        extracted_text = textract_client.get_multi_analyze_id(
            file_names=[insurance_front_path, insurance_back_path]
        )

        self._extracted_info = extracted_text if extracted_text is not None else {}

        json_key = rename_file(insurance_front_path, '.jpg', '.json')
        json_key = rename_file(json_key, '.JPG', '.json')
        json_key = rename_file(json_key, '.png', '.json')
        json_key = rename_file(json_key, '.PNG', '.json')
        json_key = rename_file(json_key, '.jpeg', '.json')
        json_key = rename_file(json_key, '.JPEG', '.json')

        s3_client.put_object(
            Key=json_key,
            Body=json.dumps(extracted_text),
            ContentType="application/json"
        )

        return True
