from config.config import config_obj
from services.dynamoDB.DynamoDB import dynamodb

class TempSession:

    def __init__(self):
        self._table = dynamodb.get_table(config_obj.get_table_name())


    def update_dynamo_item(self, event=None, update_exp="", exp_attr_name={}, exp_attr_value={}):
        key_obj = {
            "id": event.get_temp_session_id()
        }
        response = None
        try:
            response = self._table.update_item(
                Key=key_obj,
                UpdateExpression=update_exp,
                ExpressionAttributeValues=exp_attr_value,
                ExpressionAttributeNames=exp_attr_name
            )
        except Exception as e:
            print(f"Error updating item: {e}")

        return response

temp_session_entity = TempSession()