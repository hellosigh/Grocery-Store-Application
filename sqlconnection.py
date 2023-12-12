import mysql.connector

def get_sql_connection():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='gs'
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
