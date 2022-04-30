from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    price = TextAreaField('Цена')
    category = TextAreaField('Категория')
    content = TextAreaField("Содержание")
    file = FileField('Вставте фото', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField('Применить')
