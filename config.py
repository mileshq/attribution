import os

#print os.environ['DATABASE_URL']

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '...and in the darkness bind them.'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    SECRET_KEY = 'uUzJAszN533Ws2feDWsUW22qzgCkbhzGZQA8gywH'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
