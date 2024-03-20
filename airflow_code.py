# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:37:28 2024

@author: shubh
"""


import logging
import airflow
from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
# from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
# from airflow.contribs.hook.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from news_fetcher_etl import runner
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# print("hello")

args = {"owner": "Airflow", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(
    dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None)

with dag:
    
    extract_news_info = PythonOperator(python_callable = runner, task_id = 'extract_news_info', dag=dag)
    
    move_file_to_s3 = BashOperator(task_id = "move_file_to_s3", 
                                   bash_command = 'aws s3 mv {{ ti.xcom_pull("extract_news_info")}} s3://YOUR_BUCKET_NAME'
                                   )
    
    snowflake_create_table = SnowflakeOperator(task_id="snowflake_create_table", 
                                               sql = """CREATE TABLE IF NOT EXISTS parquet_table USING 
                                               TEMPLATE(SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*)) FROM TABLE(
                                                   INFER_SCHEMA(LOCATION=>'@YOUR_DATABASE_NAME', 
                                                                FILE_FORMAT=>'parquet_format))) """
                                                )
    snowflake_copy = SnowflakeOperator(
        task_id = "snowflake_copy",
        sql = """COPY INTO YOUR_TABLE_NAME FROM @YOUR_DATABASE_NAME
        MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE FILE_FORMAT=parquet_format""", snowflake_conn_id = "snowflake_conn")


    extract_news_info >> move_file_to_s3 >> snowflake_create_table >> snowflake_copy                                                                                                           
                