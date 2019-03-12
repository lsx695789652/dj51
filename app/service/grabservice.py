# coding:utf-8
from bs4 import BeautifulSoup

import psycopg2
import logging

def insert_hisq_data(row):
    connection = psycopg2.connect(host='localhost', user='postgres', password='111111', database='test', port='5432',
                                  charset='utf-8')
    row['name'] = 'test'
    try:
        with connection.cursor() as cur:
            sql = 'insert into app_user(name) values (%s)'
            cur.execute(sql, row)
            connection.commit()
    except psycopg2.DatabaseError as error:
        connection.rollback()
    finally:
        connection.close()
