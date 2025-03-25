import pandas as pd
from extract.extract_base import ExtractBase
from pandas import read_csv

class ExtractFile(ExtractBase):

    def __init__(self,file_path):
        self.file_path = file_path

    def load_data(self):
        # return pd.read_csv(self.file_path)
        return read_csv(self.file_path, parse_dates=[0], index_col=0)