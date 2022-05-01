#!/usr/bin/python
import psycopg2

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

    cur.execute("SELECT * FROM customers WHERE customer_id = 1000 ORDER BY customer_name")
    print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

    cur.execute("SELECT * FROM customers WHERE customer_id = 2000 ORDER BY customer_id")
    print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

    cur.execute("SELECT * FROM customers WHERE customer_id = 3000 ORDER BY customer_id")
    print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()

    cur.execute("SELECT * FROM customers WHERE customer_id = 4000 ORDER BY customer_id")
    print("The number of parts: ", cur.rowcount)
    row = cur.fetchone()

    while row is not None:
        print(row)
        row = cur.fetchone()
    cur.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
