from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    text = TextAreaField("Text", [validators.DataRequired()])
    submit = SubmitField("Create")
    tags = SelectMultipleField("Tags", coerce=int)


class EditArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    text = TextAreaField("Text", [validators.DataRequired()])
    submit = SubmitField("Save Changes")
    tags = SelectMultipleField("Tags", coerce=str)


