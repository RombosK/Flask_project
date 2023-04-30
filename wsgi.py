from werkzeug.security import generate_password_hash
from blog.app import app, db
from datetime import datetime
import os
from blog.models import User


# app = create_app()


@app.cli.command("create-users", help="create users")
def create_users():
    """
        Run in your terminal:
        ➜ flask create-users
    """
    from blog.models import User
    db.session.add(
        User(username="test_1", email="test_1@gb.gb", is_staff=True, password=generate_password_hash("test_1")))
    db.session.add(User(username="test_2", email="test_2@gb.gb", password=generate_password_hash("test_2")))
    db.session.commit()


@app.cli.command("create-articles", help="create articles")
def create_articles():
    """
        Run in your terminal:
        ➜ flask create-articles
    """
    from blog.models import Article
    text = 'Программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM. Служит для синхронизации объектов Python и записей реляционной базы данных.SQLAlchemy позволяет описывать структуры баз данных и способы взаимодействия с ними на языкеPython без использования SQL.Система управления базами данных, СУБД — совокупность программных и лингвистических средств общего или специального назначения, обеспечивающих управление созданием и использованием базданных.ORM — технология программирования, которая связывает базы данных с концепциямиобъектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных».'
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
    #     from blog.models import User
    #     admin = User(username="admin", email="admin@gb.gb", is_staff=True)
    #     # test_1 = User(nickname="test_1", email="test_1@gb.gb", is_staff=False)
    #     db.session.add(admin)
    #     # db.session.add(test_1)
    #     db.session.commit()
    #     print("done! created users:", admin)

    from blog.extension import db
    from blog.models import User
    admin = User(username='superadmin',first_name="super", last_name="superoff", email='test_admin@email.com', is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'superadmin'
    db.session.add(admin)
    db.session.commit()
    print('created superadmin:', admin)
