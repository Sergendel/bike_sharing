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
│   └── batch1.csv
├── extract
│   ├── extract_base.py
│   └── extract_file.py    
├── notebook
│   └── Bike_sharing_Model_build
├── models
│   ├── model_casual.pkl
│   └── model_registered.pkl    
├── transform
│   ├── transform_model.py
│   └── transform_processing.py
├── Dockerfile
├── .dockerignore
├── main.py
├── requirements.txt
├── Dockerize_the_Solution.md
└── README.md
```

## How to Run

Install dependencies:
```bash
pip install -r requirements.txt
```

### Model Inference
Run inference with:
```bash
python main.py
```

### Docker Deployment

Run the Docker container, mounting an output folder:
```bash
docker run -it -v "$(pwd)/output":/app/output bike_sharing:v1
```

The output folder will contain the resulting CSV file with predictions under the column `count_predict`.

---

## Dockerization Steps

### Step 1: Python Environment Setup

Set up a Python environment with all required dependencies:

```bash
conda create -n env python=3.7.6
conda activate env
pip install -r requirements.txt
```

### Step 2: Docker Image Builds

Three Docker images were built to demonstrate various scenarios:

#### 1. Simple Docker Build (No volumes)

```bash
docker build . -t bike_sharing:v1

docker images
docker images | grep -i bike

docker run -it bike_sharing:v1
# OR
docker run -itd bike_sharing:v1
```

- `-i`: Interactive mode, allows input.
- `-t`: Allocates a pseudo-terminal.
- `-d`: Detached mode; container runs in the background.

Additional Docker commands:
```bash
docker ps -a

docker run -itd bike_sharing:v1 bash
docker exec -it <container_id> bash
docker exec -it <container_id> python main.py

exit  # terminates the shell session

docker rm -f <container_id>
# OR stop first:
docker stop <container_id>
```

#### 2. Docker Build with Data Mounted from Volume

Adds `./data` to `.dockerignore` and mounts the data folder:

```bash
echo "./data" >> .dockerignore
docker build . -t bike_sharing:v2
```

Run Docker container with mounted data:
```bash
docker run -it -v ./data/:/app/data bike_sharing:v2
```

Windows users (full path or Git Bash):
```bash
docker run -it -v "C:\work\Mlops\Model Deployment\Exercise\Bike_Sharing\data":/app/data bike_sharing:v2 bash
# OR
winpty docker run -it -v "$(pwd)/data":/app/data bike_sharing:v2 bash
```

#### 3. Docker Build with Configuration File Loaded from Volume

Now both data and config file are included in `.dockerignore` and mounted:

```bash
echo "config.py" >> .dockerignore
docker build . -t bike_sharing:v3
```

Run container with both data and configuration mounted:

```bash
docker run -it -v "$(pwd)/data":/app/data -v "$(pwd)/config.py":/app/config.py bike_sharing:v3 bash
# OR

docker run -it --mount type=bind,source="$(pwd)/config.py",target=/app/config.py bike_sharing:v3
```

---

### Step 3: Push to Docker Hub

Demonstration using Lev's lectures:

#### Run container with MySQL (example of using environment variables)

```bash
docker rm -f mysql-docker-local
docker run -p 13306:3306 --name mysql-docker-local -e MYSQL_ROOT_PASSWORD=Password -d mysql:latest
docker exec -it <container_id> bash
env
```

#### Push Docker image to Docker Hub

```bash
docker tag bike_sharing:v3 313733172/bike_sharing:v3
docker tag bike_sharing:v2 313733172/bike_sharing:v2
docker tag bike_sharing:v1 313733172/bike_sharing:v1

docker login
docker push 313733172/bike_sharing:v3
```

#### Run on [Play with Docker](https://labs.play-with-docker.com/)

```bash
docker login -u 313733172
docker pull 313733172/bike_sharing:v1
```

---