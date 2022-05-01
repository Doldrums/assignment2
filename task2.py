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

    commands = [
        """
                    CREATE TABLE customers (
                        customer_id SERIAL PRIMARY KEY,
                        customer_name VARCHAR(255) NOT NULL,
                        customer_address VARCHAR(255) NOT NULL,
                        customer_review VARCHAR(255) NOT NULL
                    )
                    """,
        """
            CREATE TABLE purchases (
                purchase_id SERIAL PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                FOREIGN KEY (customer_id)
                    REFERENCES customers (customer_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
                """
                CREATE TABLE products (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                                            product_details VARCHAR(255) NOT NULL,
                                            product_price INTEGER NOT NULL,
                                            product_type VARCHAR(255) NOT NULL
                                        )
                                        """,
                """
                        CREATE TABLE purchases_products_list (
                            purchases_products_list_id SERIAL PRIMARY KEY,
                            purchase_id INTEGER NOT NULL,
                            FOREIGN KEY (purchase_id)
                                REFERENCES purchases (purchase_id)
                                ON UPDATE CASCADE ON DELETE CASCADE,
                            product_id INTEGER NOT NULL,
                            FOREIGN KEY (product_id)
                                REFERENCES products (product_id)
                                ON UPDATE CASCADE ON DELETE CASCADE
                        )
                """,
                """
                                     CREATE TABLE sales (
                                         sale_id SERIAL PRIMARY KEY,
                                         sale_discount INTEGER NOT NULL,
                                         sale_type VARCHAR(255) NOT NULL
                                     )
                                     
                                     """]

    for command in commands:
        cur.execute(command)
    conn.commit()

    sql = "INSERT INTO customers(customer_name, customer_address, customer_review) VALUES(%s,%s,%s)"
    list = []
    faker = Faker()
    for x in range(0, 10):
        random_string = ''
        for _ in range(10):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))
        inner_list = (names.get_first_name(), faker.ipv4(), random_string,)
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()

    sql = "INSERT INTO purchases(customer_id) VALUES(%s)"
    list = []
    for x in range(1, 10):
        inner_list = (x,)
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()

    sql = "INSERT INTO products(product_name, product_details, product_price, product_type) VALUES(%s,%s,%s,%s)"
    list = []
    for x in range(1, 10):
        inner_list = (names.get_first_name(), names.get_first_name(), x, names.get_first_name())
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()

    sql = "INSERT INTO purchases_products_list(purchase_id, product_id) VALUES(%s,%s)"
    list = []
    for x in range(1, 10):
        inner_list = (x, x,)
        list.append(inner_list)
    print(list)
    cur.executemany(sql, list)
    # commit the changes to the database
    conn.commit()

    sql = "INSERT INTO sales(sale_discount, sale_type) VALUES(%s,%s)"
    list = []
    for x in range(1, 10):
        inner_list = (10, 'qwerty')
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
