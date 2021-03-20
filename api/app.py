from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from api.config import env_config
api = Api()
jwt = JWTManager()
def create_app(config_name):
    import resources
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])
    api.init_app(app)    
    jwt.init_app(app)
    return app