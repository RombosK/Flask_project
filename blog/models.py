from flask_login import UserMixin
from sqlalchemy import ForeignKey, Integer, String, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .article_tag import article_tag_association_table
from .extension import db, flask_bcrypt_


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False, default="", server_default="")
    first_name = db.Column(db.String(120), nullable=False, default="", server_default="")
    last_name = db.Column(db.String(120), nullable=False, default="", server_default="")
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), unique=True, nullable=True, default="", server_default="")
    _password = db.Column(db.LargeBinary, nullable=True)

    author = relationship('Author', uselist=False, back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt_.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt_.check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    text = db.Column(db.String(1024))
    published_date = db.Column(db.DateTime, default=datetime.now())
    # author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # author: Mapped["User"] = relationship()
    author_id = db.Column(db.Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='articles')
    tags = relationship(
        "Tag",
        secondary=article_tag_association_table,
        back_populates="articles",
    )


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    # articles = relationship('Article', primaryjoin='Author.id == Article.author_id')
    articles = relationship('Article', back_populates='author')


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")
    articles = relationship(
        "Article",
        secondary=article_tag_association_table,
        back_populates="tags",
    )
