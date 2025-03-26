# Model Deployment (Batch) Project - Bike Sharing Prediction

## Overview

This repository contains an MLOps project demonstrating batch model deployment.  
The detailed project task is described in the file `MLOp Exercise.docx`.

## Workflow

The project implements the following workflow:

1. Extract data from, e.g., `data/batch_1.csv`
2. Process data
3. Load trained models
4. Perform inference
5. Save predictions to `output/batch_1_prediction.csv`

The Docker run command should include mounting an output folder to save the prediction file.

## Repository Structure

```
bike_sharing
├── data
    └── batch1.csv
├── extract
    └── exract_base.py
    └── exract_file.py    
├── notebook
    └── Bike_sharing_Model_build
├── models
    └── model_casual.pkl
    └── model_registered.pkl    
├── transform
    └── transform_model.py
    └── transform_processing.py
├── Dockerfile
├── .dockerignore
├── main.py
├── requirements.txt
└── README.md
```

## how to run 
pip install -r requirements.txt

### Model Inference
python main.py


### Running the Docker Container

docker run -it -v "$(pwd)/output":/app/output bike_sharing:v1

### the output folder will include the resulting CSV file with predictions in column count_predict



### Docker Deployment

# 1. Sets up a Python environment with all required dependencies.
    conda create -n env python=3.7.6`  # Creates env with specific Python version      Don’t need the Python version pre-installed  on the system  
    conda activate env                 # Activate  environment                                          
    pip install -r requirements.txt`   # Install any packages Conda skipped            


# Three docker images were buils with and without vlumes mounting
  1. Simple build with no volumes, image runs as it is      --------------------------------------
  
      docker build . -t bike_sharing:v1               # build image;  . for current folder,  -t for tag. v1 is the version tag. If omitted, Docker defaults to latest. 
      docker images                                   # list images
      docker images  | grep -i bike                   # -i: ignores the letter case.
      docker run -it bike_sharing:v1                  # OR
      
      docker run --name bike_sharing_v1 -itd bike_sharing:v1                 #  In the command docker run -itd:
                                                      #    -i: Interactive mode, allowing input.
                                                      #    -t: Allocates a pseudo-terminal.
                                                      #    -d: Detached mode; container runs in the background.
                                                      # Thus, docker run -itd starts an interactive container session running detached,
                                                      # letting the container operate independently in the background.                                                   
  
      docker ps -a                                    # containers, -a for all even the stopped  
  
      # run docker and bash
      docker run --name bike_sharing_v1 -it bike_sharing:v1 bash
      docker exec -it <container id> bash              # new interactive bash shell session inside the already-running Docker container.
      docker exec -it <container id> python main.py
  
      exit                                             # terminates that specific shell session, returning you to your original terminal or environment                      
  
      docker rm -f <contaier_id>                       # remove , -f to force , as container is running. or first stop it by 
      docker stop <container_id_or_name>
  
  
  2. data loaded from volume , adds ./data to dockerignore and mount data folder to app/data on container                         
     echo "./data" >> .dockerignore                            # Appends ./data to .dockerignore, creating the file if it doesn't exist.
     docker build . -t bike_sharing:v2
     docker run --name bike_sharing_v2 -it -v ./data/:/app/data bike_sharing:v2       # would not work in gitbash
     # on windows you should run wth full path
     docker run --name bike_sharing_v2 -it -v "C:\work\Mlops\Model Deployment\Exercise\Bike_Sharing\data":/app/data bike_sharing:v2 bash
     winpty docker run -it -v "$(pwd)/data":/app/data bike_sharing:v2 bash
  
  
  3. config file loaded from volume . now both folder data and file config are in ignore and should be mounted                        
     echo "config.py" > .dockerignore                  # Appends ./data to .dockerignore, creating the file if it doesn't exist.
     docker build . -t bike_sharing:v3
     docker run --name bike_sharing_v3 -it -v "$(pwd)/data":/app/data  -v "$(pwd)/config.py":/app/config.py  bike_sharing:v3 bash   # now both data and config are mounted
  
     docker run -it --mount type=bind,source="$(pwd)/config.py",target=/app/config.py bike_sharing:v3
  

# 3. push to dockerhub (used Lev's lectures)
    1. run container with mysql , sow hot to use env variables
        docker rm -f mysql-docker-local
        docker run -p 13306:3306 --name mysql-docker-local -e MYSQL_ROOT_PASSWORD=Password -d mysql:latest
        docker exec -it b67bf66e44c128647cc008552e55946dfb1b52d5f18cea189c1f81826ec0c5fd bash
        env
    2. how to push image to dockerhub
       docker tag bike_sharing:v3 313733172/bike_sharing:v3
       docker tag bike_sharing:v2 313733172/bike_sharing:v2
       docker tag bike_sharing:v1 313733172/bike_sharing:v1
       docker login 
       docker push 313733172/bike_sharing:v3

    3. run on  https://labs.play-with-docker.com/   
        docker login -u 313733172
        docker pull 313733172/bike_sharing:v1


## PostgreSQL Container Setup

### Step 1: Docker Container with PostgreSQL

Ensure your PostgreSQL Docker container (`bike_postgres`) is running:

```bash
docker run --name bike_postgres -e POSTGRES_PASSWORD=serg -p 5432:5432 -d postgres
```

| Parameter   | Meaning                                                          |
|-------------|------------------------------------------------------------------|
| `--name`    | Container name you assign (`bike_postgres`)                      |
| `-e`        | Environment variable (`POSTGRES_PASSWORD`)                       |
| `-p`        | Port mapping (`host_port:container_port`)                        |
| `-d`        | Detached mode (runs container in background)                     |
| `postgres`  | The official Docker Hub image for PostgreSQL                     |

Make sure:
- The PostgreSQL container (`bike_postgres`) is actively running.
- PostgreSQL is accessible on port `5432`.

### Step 2: Create the Database

Before loading data, create the target database (`bike_sharing`):

```bash
docker exec -it bike_postgres psql -U postgres -c "CREATE DATABASE bike_sharing;"
```
OR
1. Enter the Docker container
```bash 
docker exec -it bike_postgres bash
```
2. Run the PostgreSQL command inside the container
```bash 
psql -U postgres -c "CREATE DATABASE bike_sharing;"
```

|Command Part                             | Explanation                                                   |
|-----------------------------------------|---------------------------------------------------------------|
| `docker exec`                           | Run a command inside an already running Docker container.     |
| `-it`                                   | Interactive (`-i`) mode with pseudo-terminal (`-t`).          |
| `bike_postgres`                         | Name of the Docker container running PostgreSQL.              |
| `psql`                                  | PostgreSQL command-line interface tool (CLI).                 |
| `-U postgres`                           | Connect to PostgreSQL using the default user (`postgres`).    |
| `-c "CREATE DATABASE bike_sharing;"`    | Execute SQL command to create the database `bike_sharing`.    |

3. List all databases :

 Enter the PostgreSQL container
```bash 
docker exec -it bike_postgres psql -U postgres
```

List all databases:
```bash 
\l
```
or explicitly:

```bash 
\list
```


### Step 3: Run Python Script Locally to Load Data into PostgreSQL (Recommended)

Run the Python script `load_csv_to_db.py` directly on your local machine, where your CSV file and Python environment are already set up.

Ensure your working directory structure is:

```
.
├── data
│   └── batch1.csv
└── load_csv_to_db.py  # your script filename
```

Install required dependencies:
```bash
pip install pandas sqlalchemy psycopg2-binary
```

Execute the Python script:
```bash
python load_csv_to_db.py
```

### Step 4: Verify Data Import

To confirm explicitly that your data is successfully loaded into the PostgreSQL database, follow these steps:

**Step 4.1:** Enter the PostgreSQL command-line interface:

```bash
docker exec -it bike_postgres psql -U postgres -d bike_sharing
```

**Step 4.2:** Verify the content of your table (`bike_sharing_data`):

```sql
SELECT * FROM bike_sharing_data LIMIT 5;
```

This command displays the first 5 rows of your populated table, confirming successful data import.

**Step 4.3:** Check the total number of rows imported:

```sql
SELECT COUNT(*) FROM bike_sharing_data;
```


### Step 5: Save resulting table to postgreSQL

```bash
docker exec -it bike_postgres psql -U postgres -d bike_sharing
```

```sql
SELECT * FROM bike_sharing_data_predictions LIMIT 5;
```