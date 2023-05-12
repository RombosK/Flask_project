from functools import wraps

from flask import Blueprint, render_template, request, url_for, redirect, abort, flash
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user

from blog import articles
from blog.forms.article import CreateArticleForm
from blog.users.views import get_user_name
from blog.extension import db
# from blog.forms.article import CreateArticleForm
from blog.models import Article, User, Author, Tag

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")
tag = Blueprint("tag", __name__, url_prefix="/tags", static_folder="../static")


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


@article.route("/<int:article_id>/", endpoint="details")
def article_details(article_id):
    article = Article.query.filter_by(id=article_id).options(joinedload(Article.tags)).one_or_none()
    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)


@article.route("/create", methods=["GET", "POST"])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]

    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.text.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        article.author_id = current_user.author.id

        db.session.add(article)
        db.session.commit()

        return redirect(url_for("article.get_article", pk=article.id))
    return render_template("articles/create.html", form=form)


@article.route("/delete/<int:pk>", methods=["POST"])
@login_required
def delete_article(pk):
    article = Article.query.get_or_404(pk)

    if article.author_id != current_user.author.id:
        abort(403)

    db.session.delete(article)
    db.session.commit()

    return redirect(url_for("article.article_list"))
