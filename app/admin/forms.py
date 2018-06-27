from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnimalForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    animal_id = StringField('ID', validators=[DataRequired()])
    sex = StringField('Sex')
    age = StringField('Age')
    submit = SubmitField('Submit')