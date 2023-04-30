from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user

from blog.forms.article import CreateArticleForm
from blog.users.views import get_user_name
from blog.extension import db
# from blog.forms.article import CreateArticleForm
from blog.models import Article, User, Author

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")


@article.route("/")
@login_required
def article_list():
    from ..models import Article
    articles = Article.query.all()
    return render_template(
        "articles/list.html",
        articles=articles
    )


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    from ..models import Article
    article = Article.query.filter_by(id=pk).one_or_none()
    if article is None:
        raise NotFound("Article id:{}, not found".format(pk))
    return render_template(
        "articles/details.html",
        article=article
    )


@article.route("/create", methods=["GET"])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template("articles/create.html", form=form)


@article.route("/create", methods=["POST"])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        _article.author_id = current_user.author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for("article.get_article", pk=_article.id))
    return render_template("articles/create.html", form=form)

