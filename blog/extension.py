from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from blog.admin.views import MyAdminIndexView

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
flask_bcrypt_ = Bcrypt()
admin = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4",
)




