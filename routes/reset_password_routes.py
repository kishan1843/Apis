#routes/reset_password_routes.py
from flask import Blueprint, request    
from controller.reset_password import reset_password

reset_password_routes = Blueprint('reset_password_routes', __name__)

@reset_password_routes.route('/reset-password', methods=['POST'])
def reset_password_route():
    return reset_password()
