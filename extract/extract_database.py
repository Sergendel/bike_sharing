import pandas as pd

import config
from extract.extract_base import ExtractBase
from sqlalchemy import create_engine

class ExtractDb(ExtractBase):

    def __init__(self,db_url):
        self.db_url = db_url

    def load_data(self):
        print("Loading data from PostgreSQL database...")
        engine = create_engine(self.db_url)
        df =pd.read_sql_table(config.TABLE_NAME, engine)
        df.set_index(pd.to_datetime(df['datetime']), inplace=True)
        return df
