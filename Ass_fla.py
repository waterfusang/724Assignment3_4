from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__) # Create Flask application object
app.config['SECRET_KEY'] = 'sk'

# Flask routes
@app.route('/') # Root route
def index():
    return render_template('Ass_WP.html')

@app.route('/Information_Page') # Information_Page route
def Information_Page():
    return render_template('Ass_IP.html')

@app.route('/Data_Collection_Page', methods=['GET', 'POST']) # Data_Collection_Page route
def Data_Collection_Page():
    form = DataCollectionForm()
    if form.validate_on_submit():
        return "Data submitted successfully"
    return render_template('Ass_DCP.html', form=form)

# Form class for data collection
class DataCollectionForm(FlaskForm):
    grades_obtained = SelectField('Grades obtained in courses', choices=[('100~80', '100~80'), ('80~60', '80~60'), ('under60', 'Under 60')], validators=[DataRequired()])
    name = StringField('User\'s name', validators=[DataRequired()])
    student_number = StringField('Student number', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired()])
    satisfaction = SelectField('Overall satisfaction with the academic experience', choices=[('good', 'Good :)'), ('medium', 'Medium *'), ('poor', 'Poor :(')], validators=[DataRequired()])
    suggestions = StringField('Suggestions for improvement')

if __name__ == '__main__': # Run the Flask application server
    app.run(debug=True)