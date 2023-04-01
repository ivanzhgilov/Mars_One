from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class EmergencyAccess(FlaskForm):
    id_astronaut = IntegerField('Id астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = IntegerField('Id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
