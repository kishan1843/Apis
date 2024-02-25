# controller/register.py
from flask import request, jsonify
from model.register import register_query

def register_routes():
    data = request.get_json()
    result, status_code = register_query(data)
    return jsonify(result), status_code