from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from blog.admin.views import MyAdminIndexView
from flask_combo_jsonapi import Api
from flask_wtf import CSRFProtect


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()
flask_bcrypt_ = Bcrypt()
admin = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4",
)
api = Api()




