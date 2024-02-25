# util/config.py
from flask import jsonify
from flask import Response

def send_success_response(data, message, status_code=200):
    response = {
        'is_successful': '1',
        'error_code': -1,
        'data': data,
        'errors': '',
        'success_message': message
    }
    return(response), status_code

def send_error_response(error_code, errors, status_code):
    response = {
        'is_successful': '0',
        'error_code': error_code,
        'data': [],
        'errors': errors,
        'success_message': ''
    }
    return(response), status_code
