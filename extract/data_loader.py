from extract.extract_base import ExtractBase
from extract.extract_file import ExtractFile
from extract.extract_database import ExtractDb

def data_loader(config):
    # Extract
    source = config.DATA_SOURCE
    if source == 'csv':
        extract: ExtractBase = ExtractFile(config.FILE_PATH)
        dataset = extract.load_data()
    elif source == 'postgres':
        extract: ExtractBase = ExtractDb(config.DATABASE_URL)
        dataset = extract.load_data()
    else:
        raise ValueError("Invalid data source. Choose 'csv' or 'postgres'.")

    return dataset