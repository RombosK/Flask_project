from blog.app import create_app
from blog.extension import db
# from wsgi import init_db

# if __name__ == "__main__":
#     app = create_app()
#     app.run(
#         host="0.0.0.0",
#         # port=8000,
#         debug=True
#     )
app = create_app()
if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0",
            debug=True)
