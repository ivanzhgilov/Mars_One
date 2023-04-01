from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class AddingJob(FlaskForm):
    job = StringField("Job Title", validators=[DataRequired])
    team_leader = IntegerField("Team Leader id", validators=[DataRequired])
    work_size = IntegerField("Work Size", validators=[DataRequired])
    collaborators = StringField("Collaborators", validators=[DataRequired])
    is_finished = BooleanField("is job finished?")
    submit = SubmitField("Submit")
