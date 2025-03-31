from flask import Flask
from .views.routes import api

def create_app():
    app = Flask(__name__)

    from .views.routes import api
    app.register_blueprint(api)

    return app
