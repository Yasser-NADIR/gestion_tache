from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class TacheForm(FlaskForm):
    libelle_tache = StringField('Libelle Tache', validators=[DataRequired(), Length(max=100)])
    coefficient = IntegerField('Coefficient', validators=[DataRequired(), NumberRange(min=0, max=999)])
    remarques = StringField('Remarques', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit')

class TacheSearchForm(FlaskForm):
    libelle_tache = StringField('Libelle Tache', validators=[Optional()])
    coefficient = StringField('Coefficient', validators=[Optional()])
    remarques = StringField('Remarques', validators=[Optional()])
    submit = SubmitField('Search')