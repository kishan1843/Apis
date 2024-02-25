# model/login.py
import hashlib
from util.database import get_mysql_connection

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def login_query(email, password):
    hashed_password = hash_password(password)

    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tbl_user WHERE email = %s AND password = %s", (email, hashed_password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user
