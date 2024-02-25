#controller/ login.py
from flask import request
from util.config import send_success_response, send_error_response
from util.database import hash_password 

from model.login import login_query

def login_route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = login_query(email, password)

    if user and hash_password(password) == user['password']:
        return send_success_response(user, "Login successfully")
    else:
        return send_error_response(401, {'error': 'Invalid credentials'}, 401)
