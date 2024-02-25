#model/forget_password.py
from util.database import get_mysql_connection

def forget_password_query(email):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM registration WHERE email = %s", (email,))
    user = cursor.fetchone()

    
    cursor.close()
    connection.close()

    return user
