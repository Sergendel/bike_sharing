import pickle
from sklearn.ensemble import RandomForestClassifier


class TransformModel():
    def __init__(self, config):
        self.config = config
        self.__load_dependency()

    def __validation(self, dataset):
        pass

    def __load_dependency(self):
        with open(self.config.MODEL_CASUAL_PATH, 'rb') as f:
            self.model_casual: RandomForestClassifier = pickle.load(f)

        with open(self.config.MODEL_REGISTERED_PATH, 'rb') as f:
            self.model_registered: RandomForestClassifier = pickle.load(f)

    def predict_count(self, dataset):
        self.__validation(dataset)
        temp_dataset = dataset[self.config.PREDICT_COLUMNS]
        casual = self.model_casual.predict(temp_dataset)
        registered = self.model_registered.predict(temp_dataset)

        result = casual + registered
        return result
