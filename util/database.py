# util/database.py
import mysql.connector
import hashlib

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'main'
}

def get_mysql_connection():
    return mysql.connector.connect(**db_config)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_password_in_data(data):
    if 'password' in data:
        data['password'] = hash_password(data['password'])
    return data

def execute_query(query, data=None, hash_password=False):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        if hash_password and data:
            data = hash_password_in_data(data)

        cursor.execute(query, data)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()