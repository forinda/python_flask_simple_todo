from flask_wtf import FlaskForm
from wtforms.fields.simple import (BooleanField,
                                   SubmitField,
                                   TextAreaField, 
                                   StringField)
from wtforms.validators import DataRequired, Length


class TodoCreationForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired(),Length(5,128)])
    done = BooleanField('done')
    submit = SubmitField('Add')


class TodoUpdateForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired(),Length(5,128)])
    submit = SubmitField('Update')
