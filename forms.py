from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class DataCollectionForm(FlaskForm):
    grades_obtained = SelectField('Grades obtained in courses', choices=[('100~80', '100~80'), ('80~60', '80~60'), ('under60', 'Under 60')])
    name = StringField('User\'s name', validators=[DataRequired()])
    student_number = StringField('Student number', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    satisfaction = SelectField('Overall satisfaction with the academic experience', choices=[('good', 'Good :)'), ('medium', 'Medium *'), ('poor', 'Poor :(')])
    suggestions = StringField('Suggestions for improvement')