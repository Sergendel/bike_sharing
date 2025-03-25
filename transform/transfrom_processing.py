from math import sin, cos, pi

class TransformProcessing():
    def __init__(self,config):
        self.config = config

    def __validation(self,dataset):
        pass

    @staticmethod
    def __explode_dt(df):
        df['year'] = df.index.year
        df['month'] = df.index.month
        df['hour'] = df.index.hour
        df['weekday'] = df.index.weekday
        return df

    @staticmethod
    def __convert_hours_to_circle_data(df):
        df['hour_x'] = df['hour'].apply(lambda x: sin(2 * pi * x / 24))
        df['hour_y'] = df['hour'].apply(lambda x: cos(2 * pi * x / 24))
        return df

    @staticmethod
    def __drop_columns(df,drop_columns):
        df.drop(drop_columns, axis=1, inplace=True)
        return df

    def transform(self, dataset):
        self.__validation(dataset)

        # Create datetime columns
        dataset = self.__explode_dt(dataset)

        # Convert hours to circle data
        dataset = self.__convert_hours_to_circle_data(dataset)

        # drop columns
        #dataset = self.__drop_columns(dataset, self.config.DROP_COLUMNS)



        return dataset