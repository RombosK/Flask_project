import os
import json
from flask import Flask
from flask_migrate import Migrate
from blog.extension import db, login_manager, flask_bcrypt_
from blog.auth.views import auth
from blog.articles.views import article
from blog.users.views import user
from blog.index.views import index
from blog.models import User


CONFIG_PATH = os.getenv("CONFIG_PATH", os.path.join('..', 'dev_config.json'))

VIEWS = [
    index,
    user,
    article,
    auth,
]


def register_extensions(app):
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    flask_bcrypt_.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, json.load)
    migrate = Migrate(app, db, compare_type=True)
    register_extensions(app)
    register_blueprints(app)
    return app









