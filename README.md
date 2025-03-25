# Bike Sharing Prediction Project

## Overview

This repository contains a machine learning project aimed at predicting bike rental counts based on historical bike-sharing data. The project demonstrates data preprocessing, feature engineering, model training, and evaluation using popular ML frameworks and techniques.

## Features

- **Data Analysis and Visualization:** Insights from historical rental data.
- **Feature Engineering:** Handling and transforming data to extract meaningful features.
- **Machine Learning Models:** Implementation and evaluation of regression algorithms.
- **Model Evaluation:** Metrics and methods for assessing model performance.
- **Dockerized Application:** Easily reproducible and deployable via Docker containers.

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
├── Dockerize the Soluton.md
└── README.md
```

## Installation & Usage

### Prerequisites

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Docker

### Set Up the Environment

Install dependencies using pip:

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Model Inference

Run the model training script:

```bash
python main.py
```

### Running the Docker Container

To build and run using Docker:

```bash
docker build -t bike_sharing .
```

Replace ports or container names as needed.

## Data Source

The dataset used for this project contains hourly and daily count data for bike rentals, enriched with weather and seasonal information. 

## Use Cases

- **Bike rental demand prediction**
- **Resource planning and management**
- **Data-driven decision making for rental businesses**

## Author

- Sergendel

---

Feel free to explore, use, or contribute to this repository!
