from werkzeug.security import generate_password_hash
from blog.app import create_app, db
from datetime import datetime

app = create_app()


@app.cli.command("init-db", help="create all db")
def init_db():
    db.create_all()


@app.cli.command("create-users", help="create users")
def create_users():
    from blog.models import User
    db.session.add(User(nickname="Python", email="test_1@gb.gb", password=generate_password_hash("test_1")))
    db.session.add(User(nickname="Flask", email="test_2@gb.gb", password=generate_password_hash("test_2")))
    db.session.commit()


@app.cli.command("create-articles", help="create articles")
def create_articles():
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
