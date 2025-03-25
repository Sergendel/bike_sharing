import os
import config

def save_result_csv(dataset, result):
    # Add result column  and save to output file
    # add columnt to the bach file
    dataset['count_pred'] = result

    # extract input file name
    base_filename = os.path.splitext(os.path.basename(config.FILE_PATH))[0]

    # create folder
    os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)

    # save CSV
    dataset.to_csv(os.path.join(config.OUTPUT_FOLDER, f"{base_filename}_prediction.csv"), index=False)