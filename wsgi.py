import os
from datetime import datetime
from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.extension import db

app = create_app()


@app.cli.command("create-users", help="create users")
def create_users():
    """
        Run in your terminal:
        ➜ flask create-users
    """
    from blog.models import User
    db.session.add(
        User(username="test_1", email="test_1@gb.gb", first_name="Test_1", last_name="Tort", is_staff=True,
             password=generate_password_hash("test_1")))
    db.session.add(User(username="test_2", email="test_2@gb.gb", first_name="Test_2", last_name="Cap",
                        password=generate_password_hash("test_2")))
    db.session.commit()


@app.cli.command("create-articles", help="create articles")
def create_articles():
    """
        Run in your terminal:
        ➜ flask create-articles
    """
    from blog.models import Article
    text = 'Программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM.' \
           'Служит для синхронизации объектов Python и записей реляционной базы данных.SQLAlchemy позволяет описывать' \
           'структуры баз данных и способы взаимодействия с ними на языкеPython без использования SQL.Система ' \
           'управления базами данных, СУБД — совокупность программных и лингвистических средств общего или ' \
           'специального назначения, обеспечивающих  управление созданием и использованием баз данных.ORM — ' \
           'технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков\
            программирования, создавая «виртуальную объектную базу данных».'
    published = True
    current_time = datetime.utcnow()
    Article.published_date = current_time

    db.session.add(Article(title='Заголовок_1', text=text, author_id=1))
    db.session.add(Article(title='Заголовок_2', text=text, author_id=2))
    db.session.add(Article(title='Заголовок_3', text=text, author_id=1))
    db.session.add(Article(title='Заголовок_4', text=text, author_id=2))
    db.session.commit()


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    flask create-admin
    """
    from blog.extension import db
    from blog.models import User
    admin = User(username='superadmin', first_name="super", last_name="superoff", email='test_admin@email.com',
                 is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'superadmin'
    db.session.add(admin)
    db.session.commit()
    print('created superadmin:', admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")

