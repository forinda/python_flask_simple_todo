from flask_wtf import FlaskForm
from wtforms.fields.simple import (BooleanField,
                                   SubmitField,
                                   TextAreaField, 
                                   StringField)
from wtforms.validators import DataRequired


class TodoCreationForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    done = BooleanField('done')
    submit = SubmitField('Add')


class TodoUpdateForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')
