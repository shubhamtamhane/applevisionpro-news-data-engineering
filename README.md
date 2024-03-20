# applevisionpro-news-data-engineering

# Automated Data Pipeline for Fetching and Processing News Articles related to Apple Vision Pro

This project implements an automated data pipeline using Python, Airflow, AWS CLI, and Snowflake database. The pipeline fetches news articles about Apple Vision Pro from a specified API, processes the data, and transfers it to Amazon S3 for storage. Subsequently, the data is loaded into a Snowflake database for further analysis.

## Features

- **Automated Data Pipeline**: The pipeline is designed to run automatically, fetching news articles on a regular schedule.
- **API Integration**: Utilizes a specified API to fetch news articles about Apple Vision Pro.
- **Data Processing**: Processes the fetched data to extract relevant information and transform it into a suitable format.
- **AWS Integration**: Uses AWS CLI commands to transfer the processed data files to Amazon S3.
- **Snowflake Integration**: Loads the data from Amazon S3 into a Snowflake database for storage and analysis.

## Installation

- Clone the repository:

   ```bash
   git clone https://github.com/shubhamtamhane/applevisionpro-news-data-engineering.git
  ```

## Configuration
- Set up an Airflow environment on an EC2 instance.
- Configure Airflow to run the data pipeline at the desired schedule.
- Configure AWS CLI with appropriate credentials for accessing Amazon S3.
- Configure Snowflake database connection details in the Airflow DAG.

## Usage
- Start Airflow scheduler and web server:
 ```bash
   airflow scheduler
   airflow webserver
```

- Access the Airflow web interface and trigger the DAG to start the data pipeline.
