#routes/login_routes.py
from flask import Blueprint, request, jsonify
from controller.login import login_route

login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/login', methods=['POST'])
def login():
    return login_route()
