from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from ..utils.users import libelle_famille_list

class UserForm(FlaskForm):
    nom = StringField('Name', validators=[DataRequired(), Length(max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=999)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=100)])
    id_f_user = SelectField('famille', choices=libelle_famille_list())
    submit = SubmitField('Submit')

class UserSearchForm(FlaskForm):
    nom = StringField('Name', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    email = EmailField('Email', validators=[Optional()])
    id_f_user = SelectField('famille', choices=libelle_famille_list())
    submit = SubmitField('Search')