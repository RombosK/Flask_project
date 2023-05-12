from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
flask_bcrypt_ = Bcrypt()
__all__ = ['db', 'login_manager', 'flask_bcrypt_']


