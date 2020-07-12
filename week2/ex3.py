import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                    password ="pynative@#29",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Students
            (student_id   CHAR(13) PRIMARY KEY,
            f_name        VARCHAR(30) NOT NULL,
            l_name        VARCHAR(30) NOT NULL,
            e_mail        VARCHAR(50)  ); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("table created successfully in PostgreSQL")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting PostgreSQL table", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")