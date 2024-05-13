def rename_file(root_name="", old_ext="", new_ext=""):
    return root_name.replace(old_ext, new_ext)

def get_insurance_template():
    return {
        "insuranceName": '',
        "policyHolderName": '',
        "memberId": '',
        "memberDOB": '',
        "insuranceType": '',
        "groupNumber": '',
        "effectiveDate": '',
        "relToPolicyHolder": 'self',
    }