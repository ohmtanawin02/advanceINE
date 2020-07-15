import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                    password ="ome0895114530",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")

    cursor = connection.cursor()
#เวลาจะ INSERT แต่ละครั้งต้องมี cursor.execute ข้างใต้ insert ทุกครั้ง
    #postgres_insert_query = ''' INSERT INTO students (student_id, f_name, l_name, e_mail) VALUES (%s,%s,%s,%s)'''
    #record_to_insert = ('6206022620039', 'Tanawin',
                        #'Jenkunnaphat', '6206022620039@fitm.kmutnb.ac.th')
    #cursor.execute(postgres_insert_query, record_to_insert)
    #record_to_insert = ('615244503094', 'tanguy',
                        #'naja', '6206022620039@fitm.kmutnb.ac.th')
    #cursor.execute(postgres_insert_query, record_to_insert)
    #record_to_insert = ('623503403323', 'sixsack',
                        #'naja', '23503403323@fitm.kmutnb.ac.th')
    #cursor.execute(postgres_insert_query, record_to_insert)
    #record_to_insert = ('627342924763', 'penthai',
                        #'nakub', '627342924763@fitm.kmutnb.ac.th') 
    #cursor.execute(postgres_insert_query, record_to_insert)
    ##############ข้างล่างคือ SUBJECT##########
    #postgres_insert_query = ''' INSERT INTO subjects (subject_id, subject_name, creadit, teacher_id) VALUES (%s,%s,%s,%s)'''
    #record_to_insert = ('060233113', 'ADVANCED COMPUTER PROGRAMMING',
                        #'3', 'AMK')
    #cursor.execute(postgres_insert_query, record_to_insert)
    ############ข้างล่างคือ Teacher table #####
    postgres_insert_query = ''' INSERT INTO Teachers (teacher_id, f_name, l_name, e_mail) VALUES (%s,%s,%s,%s)'''
    record_to_insert = ('AMK', 'Anirach',
                        'Mignkwan', 'anirach@kmutnb.fitm.ac.th')
    cursor.execute(postgres_insert_query, record_to_insert)
    

    connection.commit()
    count = cursor.rowcount
    print(count,'Record inserted successfully into students table')

except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into students table", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")