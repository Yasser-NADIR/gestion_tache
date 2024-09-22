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
    id_h_l_ent_tache = IntegerField('IDHLEntTache', validators=[Optional()])
    id_tache = SelectField('IDTache',choices=get_nom_tache() ,validators=[Optional()], render_kw={"class": "id_tache"})
    h_debut = TimeField('HDebut',validators=[Optional()], render_kw={"class": "h_debut"})
    h_fin = TimeField('HFin',validators=[Optional()], render_kw={"class": "h_fin"})
    temps_diff = IntegerField('TempsDiff',validators=[Optional()], render_kw={"class": "temps_diff"})
    coefficient = IntegerField('Coefficient',validators=[Optional()], render_kw={"class": "coefficient"})
    prix_calc = IntegerField('PrixCalc',validators=[Optional()], render_kw={"class": "prix_calc"})
    remarques = StringField('Remarques',validators=[Optional()])