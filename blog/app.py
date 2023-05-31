import os

from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask
from blog.extension import db, login_manager, flask_bcrypt_, csrf, admin, migrate, api
from blog.models import User

CONFIG_PATH = os.getenv("CONFIG_PATH", os.path.join('..', 'config.py'))


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_extensions(app)
    register_blueprints(app)
    register_api_routes()
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    flask_bcrypt_.init_app(app)
    admin.init_app(app)
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    api.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_api_routes():
    from blog.api.tag import TagList
    from blog.api.tag import TagDetail
    from blog.api.user import UserList
    from blog.api.user import UserDetail
    from blog.api.author import AuthorList
    from blog.api.author import AuthorDetail
    from blog.api.article import ArticleList
    from blog.api.article import ArticleDetail

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_blueprints(app: Flask):
    from blog.index.views import index
    from blog.auth.views import auth
    from blog.users.views import user
    from blog.articles.views import article
    from blog.author.views import author
    from blog import admin

    app.register_blueprint(index)
    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(author)

    admin.register_views()
