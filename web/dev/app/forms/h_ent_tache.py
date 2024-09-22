from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Optional
from ..utils import get_all_nom_user

class HEntTacheForm(FlaskForm):
    libelle_journee = StringField('LibelleJournee',validators=[DataRequired()])
    id_users = IntegerField('Nom',validators=[DataRequired()])
    date_operation = DateField('DateOperation',format='%Y-%m-%d',validators=[DataRequired()])
    remarques = StringField('Remarques',validators=[DataRequired()])
    submit = SubmitField('Submit')

class HEntTacheSearchForm(FlaskForm):
    libelle_journee = StringField('Libelle Journee',validators=[Optional()])
    users = SelectField('Nom', choices=get_all_nom_user())
    date_operation = DateField('DateOperation',format='%Y-%m-%d',validators=[Optional()])
    remarques = StringField('Remarques',validators=[Optional()])
    submit = SubmitField('Submit')