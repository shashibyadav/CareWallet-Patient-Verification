
class Event:

    def __init__(self, event):
        self._user_photo_path = event['userPhoto'] if 'userPhoto' in event else None
        self._id_front_path = event['govIDFront'] if 'govIDFront' in event else None
        self._id_back_path = event['govIDBack'] if 'govIDBack' in event else None
        self._insurance_front_path = event['insuranceFront'] if 'insuranceFront' in event else None
        self._insurance_back_path = event['insuranceBack'] if 'insuranceBack' in event else None
        self._temp_session_id = event['id'] if 'id' in event else None
        self._insurance_name = event['insuranceName'] if 'insuranceName' in event else None
        self._policy_holder_name = event['policyHolderName'] if 'policyHolderName' in event else None
        self._member_id = event['memberID'] if 'memberID' in event else None
        self._member_dob = event['memberDOB'] if 'memberDOB' in event else None
        self._insurance_type = event['insuranceType'] if 'insuranceType' in event else None
        self._group_number = event['groupNumber'] if 'groupNumber' in event else None
        self._effective_date = event['effectiveDate'] if 'effectiveDate' in event else None
        self._rel_to_policy_holder = event['relToPolicyHolder'] if 'relToPolicyHolder' in event else None
        self._status = event['status'] if 'status' in event else None
        self._verified = False
        self._face_cropped = False

    def get_face_cropped(self):
        return self._face_cropped

    def set_face_cropped(self, face_cropped):
        self._face_cropped = face_cropped

    def get_verified(self):
        return self._verified

    def set_verified(self, verified):
        self._verified = verified

    def get_temp_session_id(self):
        return self._temp_session_id

    def get_policy_holder_name(self):
        return self._policy_holder_name

    def get_member_id(self):
        return self._member_id

    def get_member_dob(self):
        return self._member_dob

    def get_group_number(self):
        return self._group_number

    def get_effective_date(self):
        return self._effective_date

    def get_status(self):
        return self._status

    def get_user_photo_path(self):
        return self._user_photo_path

    def get_id_front_path(self):
        return self._id_front_path

    def get_id_back_path(self):
        return self._id_back_path

    def get_insurance_front_path(self):
        return self._insurance_front_path

    def get_insurance_back_path(self):
        return self._insurance_back_path

    def get_insurance_name(self):
        return self._insurance_name

    def get_insurance_type(self):
        return self._insurance_type

    def get_rel_policyholder_name(self):
        return self._rel_to_policy_holder
