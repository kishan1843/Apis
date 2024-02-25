from flask import Flask, request, abort
from routes import route

app = Flask(__name__)

SECRET_KEY = 'ltnfvh18zxItOhP2qzrtynnVvbyniu'

@app.before_request
def authenticate():
    auth_key = request.headers.get('Authorization')

    if auth_key != SECRET_KEY:
        abort(401)  

route.configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
