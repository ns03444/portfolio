# blogs/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = StringField('Description')
    file = FileField('Upload PDF file', validators=[FileAllowed(['pdf'])])
    submit = SubmitField("Post")