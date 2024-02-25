# model/reset_password.py

from util.database import get_mysql_connection

def verify_email_otp(email, otp):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tbl_user WHERE email = %s AND otp = %s", (email, otp))
    user = cursor.fetchone()
    print(user)
    cursor.close()
    connection.close()

    return user

def reset_password_query(password, email):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    print(email, password)
    cursor.execute("UPDATE tbl_user SET password = %s WHERE email = %s", (password, email))
    connection.commit()

    cursor.close()
    connection.close()
