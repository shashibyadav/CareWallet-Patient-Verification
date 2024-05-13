import boto3
from config.config import config_obj

class Rekognition:

    def __init__(self):
        self._client = boto3.client('rekognition')

    def get_client(self):
        return self._client

    def detect_face(self, name=""):
        return self._client.detect_faces(
            Image={
                "S3Object": {
                    "Bucket": config_obj.get_bucket_name(),
                    "Name": name
                }
            },
            Attributes=["DEFAULT"]
        )

    def compare_face(self, source="", destination="", threshold=75):
        return self._client.compare_faces(
            SimilarityThreshold=threshold,
            SourceImage={
                "S3Object": {
                    "Bucket": config_obj.get_bucket_name(),
                    "Name": source
                }
            },
            TargetImage={
                "S3Object": {
                    "Bucket": config_obj.get_bucket_name(),
                    "Name": destination
                }
            }
        )



rekognition_obj = Rekognition()