from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddOwner(FlaskForm):
    
    name = StringField('Owner\'s name: ')
    puppy_id = IntegerField('Id number of adopted puppy: ')
    submit = SubmitField('Add owner')