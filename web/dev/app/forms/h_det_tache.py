from flask_wtf import FlaskForm
from wtforms import IntegerField, TimeField, StringField, SelectField
from wtforms.validators import Optional, DataRequired
from ..utils import get_nom_tache

class HDetTacheForm(FlaskForm):
    id_h_l_ent_tache = IntegerField('IDHLEntTache',validators=[DataRequired()])
    id_tache = SelectField('IDTache',choices=get_nom_tache() ,validators=[DataRequired()])
    h_debut = TimeField('HDebut',validators=[DataRequired()])
    h_fin = TimeField('HFin',validators=[DataRequired()])
    temps_diff = IntegerField('TempsDiff',validators=[DataRequired()])
    coefficient = IntegerField('Coefficient',validators=[DataRequired()])
    prix_calc = IntegerField('PrixCalc',validators=[DataRequired()])
    remarques = StringField('Remarques',validators=[DataRequired()])

class HDetTacheSearchForm(FlaskForm):
    id_h_l_ent_tache = IntegerField('IDHLEntTache',validators=[Optional()])
    id_tache = SelectField('IDTache',choices=get_nom_tache() ,validators=[Optional()])
    h_debut = TimeField('HDebut',validators=[Optional()])
    h_fin = TimeField('HFin',validators=[Optional()])
    temps_diff = IntegerField('TempsDiff',validators=[Optional()])
    coefficient = IntegerField('Coefficient',validators=[Optional()])
    prix_calc = IntegerField('PrixCalc',validators=[Optional()])
    remarques = StringField('Remarques',validators=[Optional()])