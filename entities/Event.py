
class Event:

    def __init__(self, event):
        self._user_photo_path = event['userPhoto']
        self._id_front_path = event['govIDFront']
        self._id_back_path = event['govIDBack']
        self._insurance_front_path = event['insuranceFront']
        self._insurance_back_path = event['insuranceBack']
        self._temp_session_id = event['id']
        self._insurance_name = event['insuranceName']
        self._policy_holder_name = event['policyHolderName']
        self._member_id = event['memberID']
        self._member_dob = event['memberDOB']
        self._insurance_type = event['insuranceType']
        self._group_number = event['groupNumber']
        self._effective_date = event['effectiveDate']
        self._rel_to_policy_holder = event['relToPolicyHolder']
        self._status = event['status']
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
