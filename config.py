import os
basedir = os.path.abspath(os.path.dirname(__file__)) #__file___ is the relative path of the module from which the file is loaded

class Config(object): #the default config which all the other configs will inherit from
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed' #need to replace with environment variable later
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] #when cd'ing into lfk, .env activates & sets DATABASE_URL to postgres://....
    RECAPTCHA_PUBLIC_KEY = os.environ['RC_SITE_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RC_SECRET_KEY']

class ProductionConfig(Config): #lfk-pro
    DEBUG = False

class StagingConfig(Config): #lfk-staging
    DEVELOPMENT = True
    DEBUG = True
    
#when u cd into lfk directory, autoenv invokes .env file, which sets the APP_SETTINGS environment variable = DevelopmentConfig
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config): #dont think I have a testing config yet
    TESTING = True
