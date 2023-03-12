# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:55:22 2023

@author: Besher
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def Q9Y261():
    return 'Q9Y261 protien'

dag = DAG('Q9Y261_1', description='Q9Y261 DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2023, 3, 15), catchup=False)

Q9Y261_operator = PythonOperator(task_id='Q9Y261_task', python_callable=Q9Y261, dag=dag)

Q9Y261_operator
