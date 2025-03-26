from transform.transfrom_processing import TransformProcessing
from transform.transform_model import TransformModel
from utils.save_result_csv import save_result_csv
from extract.data_loader import data_loader
import config

def main():

    #extract data
    dataset = data_loader(config)


    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)

    # predict
    model = TransformModel(config)
    result = model.predict_count(dataset_transform)

    # load
    print(result)

    # Add result column  and save to output file or database
    save_result_csv(dataset, result)






if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
