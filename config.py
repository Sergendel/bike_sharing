DATA_SOURCE = 'postgres'  # options: 'csv' or 'postgres'

#postgres
DATABASE_URL = 'postgresql://postgres:serg@localhost:5432/bike_sharing'

#csv
#FILE_PATH = 'data/bike sharing train.csv'
FILE_PATH = 'data/batch1.csv'

# output folder
OUTPUT_FOLDER= 'output'

# Transform
MODEL_CASUAL_PATH = 'models/model_casual.pkl'
MODEL_REGISTERED_PATH = 'models/model_registered.pkl'
DROP_COLUMNS = ['atemp','season','holiday','weekday','hour']
PREDICT_COLUMNS = ['year','month','hour_x','hour_y','temp','humidity','windspeed']

