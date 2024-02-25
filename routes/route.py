#routes/route.py
from flask import Blueprint
from routes.login_routes import login_routes
from routes.register_routes import register_route
from routes.forget_password_routes import forget_password_routes
from routes.reset_password_routes import reset_password_routes

def configure_routes(app):
    app.register_blueprint(login_routes)
    app.register_blueprint(register_route)
    app.register_blueprint(forget_password_routes)
    app.register_blueprint(reset_password_routes)
