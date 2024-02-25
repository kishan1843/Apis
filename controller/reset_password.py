# controller/reset_password.py
from flask import request,jsonify
from model.reset_password import verify_email_otp, reset_password_query
from util.config import send_success_response, send_error_response
def reset_password():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')
    password = data.get('password')

    try:
        # Verify email and OTP
        user = verify_email_otp(email, otp)
        print(user)
        if user:
            # Reset password if email and OTP match
            reset_password_query(password, email)
            return send_success_response(user, "Password reset successful")
        else:
            # Return error if email and OTP do not match
            return send_error_response(user,400, "Invalid email or OTP")
    except Exception as e:
        # Return error response for any exceptions
        return send_error_response(user,500, {'error': str(e)})
 