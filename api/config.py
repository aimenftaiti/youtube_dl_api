import os
import api.secret_key as secret
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = secret.SECRET_KEY
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY="GGggjjjfk887856$%kk"
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    pass

env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}