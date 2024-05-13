
class Config:

    def __init__(self):
        self._bucket_name = "carewallet"
        self._folder_name = "temp/"
        self._region_name = "us-east-1"
        self._table_name = "temp-session-data"

    def get_bucket_name(self):
        return self._bucket_name

    def get_folder_name(self):
        return self._folder_name

    def get_region_name(self):
        return self._region_name

    def get_table_name(self):
        return self._table_name

config_obj = Config()