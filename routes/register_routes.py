#routes/register_routes.py
from flask import Blueprint, request
from controller.register import register_routes

register_route = Blueprint('register_routes', __name__)

@register_route.route('/register', methods=['POST'])
def register():
    return register_routes()
