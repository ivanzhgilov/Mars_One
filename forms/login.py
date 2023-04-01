from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    position = StringField("Должность", validators=[DataRequired()])
    speciality = StringField("Проффесия", validators=[DataRequired()])
    address = StringField("Адрес", validators=[DataRequired()])
    submit = SubmitField('Войти')
