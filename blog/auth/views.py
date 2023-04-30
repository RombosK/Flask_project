from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from blog.models import User
from blog.forms.user import RegistrationForm, LoginForm
from blog.extension import db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")

@auth.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():

    if current_user.is_authenticated:
        return redirect("home")
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
        )
        user.password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("home"))
    return render_template("auth/register.html", form=form, error=error)

@auth.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect("login")

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="username doesn't exist")
        if not user.validate_password(form.password.data):
            return render_template("auth/login.html", form=form, error="invalid username or password")
        login_user(user)
        return redirect(url_for("user.profile", pk=user.id))
    return render_template("auth/login.html", form=form)

@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))

@auth.route("/login-as/", methods=["GET", "POST"], endpoint="login-as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound
@auth.route("/secret/")
@login_required
def secret_view():
    return "Closed data for admin"




