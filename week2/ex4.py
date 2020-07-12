import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                                    password ="pynative@#29",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")

    cursor = connection.cursor()

    postgres_insert_query = '''