import datetime
from flask import render_template, request, redirect, url_for
from flask import current_app as app
from sqlalchemy import and_
from ..forms import HTacheForm, HEntTacheSearchForm
from ..models import HEntTache, HDetTache
from ..utils import get_nom_user_by_id, get_num_tache
from .. import db

@app.route('/h_taches', methods=['GET', 'POST'])
def h_taches():
    print('hello world')
    search_form = HEntTacheSearchForm()
    h_ent_taches = HEntTache.query.all()
    if request.method == 'POST' and search_form.validate_on_submit():
        h_ent_taches = HEntTache.query.filter(
            and_(
                HEntTache.libelle_journee.like(f'%{search_form.libelle_journee.data}%'),
                HEntTache.date_operation.like(f'%{search_form.date_operation.data}%'),
                HEntTache.remarques.like(f'%{search_form.remarques.data}%'),
                HEntTache.id_users.like(f'%{search_form.users.data}%')
            )
        ).all()
    return render_template('h_taches/h_taches.html', search_form=search_form, h_ent_taches=h_ent_taches, nom_user=get_nom_user_by_id, num_tache=get_num_tache)

@app.route('/add_h_taches', methods=['GET', 'POST'])
def add_h_taches():
    form = HTacheForm()
    if request.method == 'POST':
        new_h_ent_tache = HEntTache(
            libelle_journee = form.ent_tache.libelle_journee.data,
            id_users = form.ent_tache.users.data,
            date_operation = form.ent_tache.date_operation.data,
            remarques = form.ent_tache.remarques.data
        )
        db.session.add(new_h_ent_tache)
        db.session.commit()
        for h_det_tache in form.det_taches:
            new_h_det_tache = HDetTache(
                id_h_l_ent_tache = new_h_ent_tache.id_h_ent_tache,
                id_tache = h_det_tache.id_tache.data,
                h_debut = h_det_tache.h_debut.data,
                h_fin = h_det_tache.h_fin.data,
                temps_diff = h_det_tache.temps_diff.data,
                coefficient = h_det_tache.coefficient.data,
                prix_calc = h_det_tache.prix_calc.data,
                remarques = h_det_tache.remarques.data
            )
            db.session.add(new_h_det_tache)
        db.session.commit()
        return redirect(url_for('h_taches'))
    return render_template('h_taches/add_h_taches.html', form=form)

@app.route('/edit_h_taches/<int:id_h_ent_tache>', methods=['GET', 'POST'])
def edit_h_taches(id_h_ent_tache):
    h_ent_tache = HEntTache.query.get_or_404(id_h_ent_tache)
    det_taches = HDetTache.query.filter_by(id_h_l_ent_tache=id_h_ent_tache).all()
    form = HTacheForm()

    if request.method == 'POST':
        h_ent_tache.libelle_journee = form.ent_tache.libelle_journee.data
        h_ent_tache.id_users = form.ent_tache.users.data
        h_ent_tache.date_operation = form.ent_tache.date_operation.data
        h_ent_tache.remarques = form.ent_tache.remarques.data
        for i, det_tache_form in enumerate(form.det_taches):
            if i < len(det_taches):
                det_tache = det_taches[i]
            else:
                det_tache = HDetTache(id_h_l_ent_tache=id_h_ent_tache)
                db.session.add(det_tache)
            det_tache.id_tache = det_tache_form.id_tache.data
            det_tache.h_debut = det_tache_form.h_debut.data
            det_tache.h_fin = det_tache_form.h_fin.data
            det_tache.temps_diff = det_tache_form.temps_diff.data
            det_tache.coefficient = det_tache_form.coefficient.data
            det_tache.prix_calc = det_tache_form.prix_calc.data
            det_tache.remarques = det_tache_form.remarques.data
        db.session.commit()
        return redirect(url_for('h_taches'))

    form.ent_tache.libelle_journee.data = h_ent_tache.libelle_journee
    form.ent_tache.users.data = f'{h_ent_tache.id_users}'
    form.ent_tache.date_operation.data = h_ent_tache.date_operation
    form.ent_tache.remarques.data = h_ent_tache.remarques

    for i, det_tache in enumerate(det_taches):
        if i >= len(form.det_taches.entries):
            form.det_taches.append_entry()
        form.det_taches[i].id_tache.data = f'{det_tache.id_tache}'
        form.det_taches[i].h_debut.data = det_tache.h_debut
        form.det_taches[i].h_fin.data = det_tache.h_fin
        form.det_taches[i].temps_diff.data = det_tache.temps_diff
        form.det_taches[i].coefficient.data = det_tache.coefficient
        form.det_taches[i].prix_calc.data = det_tache.prix_calc
        form.det_taches[i].remarques.data = det_tache.remarques
    return render_template('h_taches/edit_h_taches.html', form=form, id=id_h_ent_tache)

@app.route('/delete_h_taches/<int:id_h_ent_tache>', methods=['GET', 'POST'])
def delete_h_taches(id_h_ent_tache):
    HEntTache.query.filter_by(id_h_ent_tache=id_h_ent_tache).delete()
    HDetTache.query.filter_by(id_h_l_ent_tache=id_h_ent_tache).delete()
    db.session.commit()
    return redirect(url_for('h_taches'))