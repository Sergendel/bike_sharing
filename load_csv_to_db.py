import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
DATABASE_URL = 'postgresql://postgres:serg@localhost:5432/bike_sharing'

# Connect to PostgreSQL
engine = create_engine(DATABASE_URL)

# Load data from CSV
df = pd.read_csv('data/batch1.csv')

# Write DataFrame to PostgreSQL (creates table if it doesn't exist)
df.to_sql('bike_sharing_data', engine, if_exists='replace', index=False)

print('Table created and populated successfully.')
