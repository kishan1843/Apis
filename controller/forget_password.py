#controller/forget_password.py
from flask import request
from model.forget_password import forget_password_query
from util.config import send_success_response, send_error_response
from util.database import get_mysql_connection
import random

def forget_password_route():
    try:
        data = request.get_json()
        email = data.get('email')

        user = forget_password_query(email)

        if user:
            # Email exists in the database, generate OTP and update it
            otp = str(random.randint(10000, 99999))
            update_generated_otp(email, otp)

            response_data = {'otp': otp}
            return send_success_response(response_data, "OTP sent successfully", 200)
        else:
            # Email not found in the database
            return send_error_response(404, "Email not found", 404)

    except Exception as e:
        return send_error_response(500, str(e), 500)

def update_generated_otp(email, otp):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM registration WHERE email = %s", (email,))
    existing_record = cursor.fetchone()

    if existing_record:
        cursor.execute("UPDATE registration SET otp = %s WHERE email = %s", (otp, email))
    else:
        pass

    connection.commit()
    cursor.close()
    connection.close()
