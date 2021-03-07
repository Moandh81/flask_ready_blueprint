from flask_wtf import FlaskForm
from wtforms.validators import  DataRequired
from wtforms import StringField, TextAreaField


class PostForm(FlaskForm):
    title = StringField("title")
    body = TextAreaField('body')