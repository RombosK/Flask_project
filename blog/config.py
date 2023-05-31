import os
from dotenv import load_dotenv
from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.PRODUCTION)
DEBUG = ENV == EnvType.DEVELOPMENT

SECRET_KEY = ')c46i=c^-in+6v4^%cw$m11m5ubaz(3vob1ffcdysa5+t@+tdj'

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

FLASK_ADMIN_SWATCH = 'cosmo'

OPENAPI_URL_PREFIX = '/api/swagger/'
OPENAPI_VERSION = '3.0.0'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.51.1'  # see version on https://cdnjs.com/libraries/swagger-ui




# import os
#
#
# class BaseConfig(object):
#     DEBUG = False
#     TESTING = False
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
#     # DATABASE_URL = "sqlite:///db.sqlite"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "abcdefg123456"
#     WTF_CSRF_ENABLED = True
#     FLASK_ADMIN_SWATCH = 'cosmo'
#     OPENAPI_URL_PREFIX = '/api/swagger'
#     OPENAPI_SWAGGER_UI_PATH = '/'
#     OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
#
#
# class DevConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
#
#
# class TestingConfig(BaseConfig):
#     TESTING = True
#
#
# class ProductionConfig(BaseConfig):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
#     SECRET_KEY = os.environ.get("SECRET_KEY")
