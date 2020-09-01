import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                    password ="ome0895114530",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="midterm")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from midtermJA"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from midtermJA table using cursor.fetchall")
    student_records = cursor.fetchmany(1)

    print("Print 2 rows")
    for row in student_records:
        print("student_id = ", row[0],)
        print("f_name = ", row[1])
        print("l_name = ", row[2])
        print("e_mail = ", row[3], "\n")
    
    student_records = cursor.fetchmany(1)

    print("Print another 2 rows")
    for row in student_records:
        print("student_id = ", row[0],)
        print("f_name = ", row[1])
        print("l_name = ", row[2])
        print("e_mail = ", row[3], "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")