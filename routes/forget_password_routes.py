#routes/forget_password_routes.py
from flask import Blueprint, request, jsonify
from controller.forget_password import forget_password_route

forget_password_routes = Blueprint('forget_password_routes', __name__)

@forget_password_routes.route('/forget-password', methods=['POST'])
def forget_password():
    return forget_password_route()
