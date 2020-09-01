import psycopg2 
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                    password ="ome0895114530",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="guestbookdb")
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE Comments
            (id           SERIAL PRIMARY KEY,
            name          VARCHAR(50) NOT NULL,
            comment       VARCHAR(1000) NOT NULL); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL")
except (Exception,psycopg2.Error) as error:
    print("Error while creating PostgreSQL table",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")