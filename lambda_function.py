import json

from entities.Event import Event
from controllers.verification.Verification import Verification
from entities.TempSession import temp_session_entity
from utils.AppWideConstants import TempSessionStatus
from controllers.insurance.InsuranceOCR import InsuranceOCR


def lambda_handler(event, context):
    event_obj = Event(event)
    verification_obj = Verification(event_obj)
    verification_obj.fraud_step()
    image, bbox = verification_obj.extract_face_from_id_image()

    similarity_threshold = 97

    if image is None:
        temp_session_entity.update_dynamo_item(
            event=event_obj,
            update_exp=f"SET #status = :status",
            exp_attr_name={
                "#status": "status"
            },
            exp_attr_value={
                ":status": TempSessionStatus.FAILED
            }
        )

        return {
            "statusCode": 1,
            "body": json.dumps({
                "message": "Rejected. no face found."
            })
        }

    cropped_id_name = verification_obj.crop_face(image, bbox)
    if cropped_id_name:
        print(f'Success! Found a face and cropped it to {cropped_id_name}.')
        event_obj.set_face_cropped(True)
    else:
        print('Did not provide a high-quality ID image.')

    similarity = verification_obj.compare_faces_simi(cropped_id_name)
    if not similarity:
        similarity = 0
    event_obj.set_verified((similarity > similarity_threshold) and event_obj.get_face_cropped())
    if event_obj.get_verified():
        print(f'Similarity of {similarity}%! You pass.')
    else:
        print(f'You are not who you say you are; only {similarity}% similar.')

    ### Insurance Verification from now
    insurance_obj = InsuranceOCR(event_obj)
    insurance_obj.ocr_extract_info()

    if event_obj.get_verified():
        temp_session_entity.update_dynamo_item(
            event=event_obj,
            update_exp=f"SET #status = :status",
            exp_attr_name={
                "#status": "status"
            },
            exp_attr_value={
                ":status": TempSessionStatus.SUCCESS
            }
        )

        return {
            "statusCode": 0,
            "body": json.dumps({
                "message": f'Congrats! You have verified your account.'
            })
        }
    else:
        temp_session_entity.update_dynamo_item(
            event=event_obj,
            update_exp=f"SET #status = :status",
            exp_attr_name={
                "#status": "status"
            },
            exp_attr_value={
                ":status": TempSessionStatus.FAILED
            }
        )

        return {
            "statusCode": 2,
            "body": json.dumps({
                "message": f'Congrats! You have verified your account.'
            })
        }