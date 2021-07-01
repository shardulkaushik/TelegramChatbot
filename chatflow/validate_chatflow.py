import pandas as pd
# from utilities.config_reader import get_attribute_str
from logger.log import log
class ValidateChatflow:

    def __init__(self, file_instance=None, file_name='chatflow.xlsx'):
        self.dataframe = None
        if file_instance is not None and 'xlsx' in file_instance.filename:
            self.dataframe = pd.read_excel(file_instance)
        else:
            self.dataframe = pd.read_csv(file_instance)

    def read_excel(self):
        if self.dataframe:
            return self.dataframe
        return None

    def to_json(self):
        if self.dataframe:
            try:
                json = self.dataframe.to_json()
                return json
            except Exception as e:
                log.exception(e)
        return None