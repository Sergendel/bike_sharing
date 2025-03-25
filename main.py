import config
from config import FILE_PATH
from extract.extract_base import ExtractBase
from extract.extract_file import ExtractFile
from transform.transfrom_processing import TransformProcessing
from transform.transform_model import TransformModel
from utils.save_result_csv import save_result_csv

def main():

    # Extract
    extract : ExtractBase = ExtractFile(FILE_PATH)
    dataset = extract.load_data()

    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)

    # predict
    model = TransformModel(config)
    result = model.predict_count(dataset_transform)

    # load
    print(result)

    # Add result column  and save to output file
    save_result_csv(dataset,result)






if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
