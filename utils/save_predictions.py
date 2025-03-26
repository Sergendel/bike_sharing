import os
import config
from sqlalchemy import create_engine
from sqlalchemy import inspect

def save_predictions(dataset, result):
    # Add result column  and save to output file
    # add column to the bach file
    dataset['count_pred'] = result

    if config.DATA_SOURCE == 'csv':
        # extract input file name
        base_filename = os.path.splitext(os.path.basename(config.FILE_PATH))[0]

        # create folder
        os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)

        # save CSV
        file_path = os.path.join(config.OUTPUT_FOLDER, f"{base_filename}_prediction.csv")
        dataset.to_csv(file_path, index=False)

        print(f"Predictions saved into file: {file_path}")

    elif  config.DATA_SOURCE == 'postgres':
        # Create PostgreSQL engine
        engine = create_engine(config.DATABASE_URL)

        # set new table name
        new_table_name = os.path.splitext(os.path.basename(config.TABLE_NAME))[0] + '_predictions'

        # Save predictions DataFrame clearly into PostgreSQL as new table
        dataset = dataset.reset_index(drop=True)
        dataset.to_sql(new_table_name, engine, if_exists='replace', index=False)

        print(f"Predictions saved into PostgreSQL table: {new_table_name}")

        # verification
        inspector = inspect(engine)

        if new_table_name in inspector.get_table_names():
            print(f"✅ Table '{new_table_name}' successfully saved in PostgreSQL.")
        else:
            print(f"❌ Table '{new_table_name}' NOT found!")