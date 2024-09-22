from flask_wtf import FlaskForm
from wtforms import FormField, SubmitField, FieldList
from . import HEntTacheSearchForm, HDetTacheSearchForm

class HTacheForm(FlaskForm):
    ent_tache = FormField(HEntTacheSearchForm)
    det_taches = FieldList(FormField(HDetTacheSearchForm),min_entries=1)
    submit = SubmitField('Submit')