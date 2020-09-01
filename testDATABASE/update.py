import psycopg2
def updateEmail(name, new_e_mail):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password ="ome0895114530",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="midterm")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from midtermJA where f_name = %s"
        cursor.execute(postgreSQL_select_Query, (name,))
        print("Before Update")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row, '\n')
        
        postgreSQL_select_Query = "update midtermJA set e_mail = %s where f_name = %s"
        cursor.execute(postgreSQL_select_Query,(new_e_mail,name,))
        connection.commit()

        postgreSQL_select_Query = "select * from midtermJA where f_name = %s"
        cursor.execute(postgreSQL_select_Query, (name,))
        print("After Update")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row, '\n')
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

updateEmail('Tanawin', 'sdsdb@ieee.org')