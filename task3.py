#!/usr/bin/python
import random

import psycopg2
from faker import Faker

""" Connect to the PostgreSQL database server """
conn = None
try:
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="amoriodi",
        password="Ihatemyself1")

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

    print('Creating tables in the PostgreSQL database...')

    command = """
            CREATE TABLE mac (
                mac_id SERIAL PRIMARY KEY,
                mac_addr VARCHAR(255) NOT NULL,
                mac_ip VARCHAR(255) NOT NULL,
                mac_country VARCHAR(255) NOT NULL,
                mac_date VARCHAR(255) NOT NULL
            )
            """

    cur.execute(command)
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')




def nextAvailable():
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="amoriodi",
        password="Ihatemyself1")
    # create a cursor
    cur = conn.cursor()
    cur.execute("SELECT MAX(mac_id) FROM mac")
    print("Next available is: ", cur.fetchone()+1)



def transform():
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="amoriodi",
        password="Ihatemyself1")
    # create a cursor
    cur = conn.cursor()


def generateData():
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="amoriodi",
        password="Ihatemyself1")
    # create a cursor
    cur = conn.cursor()
    sql = "INSERT INTO mac(mac_addr, mac_ip, mac_country, mac_date) VALUES(%s,%s,%s, %s)"
    list = []
    faker = Faker()
    for x in range(0, 1000000):
        mac_add = "02:00:00:%02x:%02x:%02x" % (random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        inner_list = (mac_add, faker.ipv4(), 'Russia', faker.date_between(start_date='today', end_date='+30y'),)
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()



def transformIP(country):
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="amoriodi",
        password="Ihatemyself1")
    # create a cursor
    cur = conn.cursor()



generateData()

