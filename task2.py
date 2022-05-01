#!/usr/bin/python
import psycopg2
import names
import random
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
            CREATE TABLE customers (
                customer_id SERIAL PRIMARY KEY,
                customer_name VARCHAR(255) NOT NULL,
                customer_address VARCHAR(255) NOT NULL,
                customer_review VARCHAR(255) NOT NULL
            )
            """

    cur.execute(command)
    conn.commit()

    sql = "INSERT INTO customers(customer_name, customer_address, customer_review) VALUES(%s,%s,%s)"
    list = []
    faker = Faker()
    for x in range(0, 1000000):
        random_string = ''
        for _ in range(10):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))
        inner_list = (names.get_first_name(), faker.ipv4(), random_string, )
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')