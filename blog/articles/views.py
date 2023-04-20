from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.users.views import get_user_name
from datetime import datetime

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../static")


TEXT = 'Some text. Description.'
ARTICLES = {
    1: {
        "title": "Number_1",
        "text": TEXT,
        "author": 1,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    2: {
        "title": "Number_2",
        "text": TEXT,
        "author": 2,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M')
    },
    3: {
        "title": "Number_3",
        "text": TEXT,
        "author": 3,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M')
    }
}

@article.route("/")
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


# @article.route("/<int:pk>")
# def get_article(pk: int):
#     if pk in ARTICLES:
#         article_raw = ARTICLES[pk]
#     else:
#         raise NotFound("Article id:{}, not found".format(pk))
#     title = article_raw["title"]
#     text = article_raw["text"]
#     author = get_user_name(article_raw["author"])
#     return render_template(
#         "articles/details.html",
#         title=title,
#         text=text,
#         author=author
#     )
@article.route("/<int:pk>")
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
        title = article_raw["title"]
        text = article_raw["text"]
        author = get_user_name(article_raw["author"])
        datetime_str = article_raw["datetime"]
        if datetime_str:
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            datetime_str = datetime_obj.strftime('%B %d, %Y %H:%M')
        return render_template(
            "articles/details.html",
            title=title,
            text=text,
            author=author,
            datetime=datetime_str
        )
    else:
        raise NotFound("Article id:{}, not found".format(pk))





