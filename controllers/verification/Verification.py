import io
from PIL import Image
from config.config import config_obj
from services.s3Client.S3Client import s3_client
from services.rekoginition.Rekognition import rekognition_obj
from utils.utils import rename_file
class Verification:

    def __init__(self, event=None, threshold=75):
        self._event = event
        self._threshold = threshold

    def fraud_step(self):
        return

    def get_bounding_box(self, response_bbox, img_width, img_height):

        left = img_width * response_bbox["Left"]
        top = img_height * response_bbox["Top"]
        width = img_width * response_bbox["Width"]
        height = img_height * response_bbox["Height"]

        return [left, top, left + width, top + height]


    def extract_face_from_id_image(self):
        id_image_path = self._event.get_id_front_path()
        response = rekognition_obj.detect_face(
            name=id_image_path
        )

        s3_response = s3_client.get_object_res(
            file_path=id_image_path
        )

        stream = io.BytesIO(s3_response["Body"].read())
        image = Image.open(stream)
        image_width, image_height = image.size

        try:
            [x1, y1, x2, y2] = self.get_bounding_box(response["FaceDetails"][0]["BoundingBox"], image_width, image_height)
            return image, [x1, y1, x2, y2]
        except:
            return None, None

    def crop_face(self, image=None, bbox=None):
        id_image_path = self._event.get_id_front_path()
        x1, y1, x2, y2 = bbox
        image = image.crop((x1, y1, x2, y2))

        buffered = io.BytesIO()
        image.save(buffered, format="PNG")

        new_fname = rename_file(id_image_path, '.jpg', '-cropped.jpg')
        new_fname = rename_file(new_fname, '.JPG', '-cropped.jpg')
        new_fname = rename_file(new_fname, '.png', '-cropped.png')
        new_fname = rename_file(new_fname, '.PNG', '-cropped.png')
        new_fname = rename_file(new_fname, '.jpeg', '-cropped.jpeg')
        new_fname = rename_file(new_fname, '.JPEG', '-cropped.JPEG')

        s3_client.put_object(
            Body=buffered.getvalue(),
            Bucket=config_obj.get_bucket_name(),
            Key=new_fname,
        )

        return new_fname

    def compare_faces_simi(self, cropped_id_path):
        user_photo_path = self._event.get_user_photo_path()
        threshold = self._threshold
        response = rekognition_obj.compare_face(
            threshold=threshold,
            source=cropped_id_path,
            destination=user_photo_path
        )
        similarity = None
        for faceMatch in response["FaceMatches"]:
            similarity = faceMatch["similarity"]
        return similarity