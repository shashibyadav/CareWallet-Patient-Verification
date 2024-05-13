import boto3


class DynamoDB:

    def __init__(self):
        self._dynamo_client = boto3.resource('dynamodb')

    def get_table(self, table_name=""):
        return self._dynamo_client.Table(table_name)


dynamodb = DynamoDB()