from flask import render_template, redirect, url_for, request, make_response, session
from .. import db
from ..models import FUser
from ..forms import FUserForm, FUserSearchForm
from flask import current_app as app
from sqlalchemy import and_
import io
import csv

@app.route('/f_users', methods=['GET', 'POST'])
def f_users():
    users = FUser.query.all()
    search_form = FUserSearchForm()
    if request.method == 'POST' and search_form.validate_on_submit():
        session['libelle_famille'] = search_form.libelle_famille.data
        session['coefficient'] = search_form.coefficient.data
        session['remarques'] = search_form.remarques.data
        users = FUser.query.filter(
            and_(
                FUser.libelle_famille.like(f'%{search_form.libelle_famille.data}%'),
                FUser.coefficient.like(f'%{search_form.coefficient.data}%'),
                FUser.remarques.like(f'%{search_form.remarques.data}%')
            )
        ).all()
    return render_template('f_users/f_users.html', users=users, search_form=search_form)

@app.route('/add_f_user', methods=['GET', 'POST'])
def add_f_user():
    form = FUserForm()
    if request.method=='POST' and form.validate_on_submit():
        new_f_user = FUser(
            libelle_famille=form.libelle_famille.data,
            coefficient=form.coefficient.data,
            remarques=form.remarques.data
        )
        db.session.add(new_f_user)
        db.session.commit()
        return redirect(url_for('f_users'))
    return render_template('f_users/add_f_user.html', form=form)

@app.route('/edit_f_user/<int:id>', methods=['GET', 'POST'])
def edit_f_user(id):
    user = FUser.query.get(id)
    form = FUserForm(obj=user)
    if request.method == 'POST' and form.validate_on_submit():
        user.libelle_famille = form.libelle_famille.data
        user.coefficient = form.coefficient.data
        user.remarques = form.remarques.data
        db.session.commit()
        return redirect(url_for('f_users'))
    return render_template('f_users/edit_f_user.html', form=form, user=user)
    

@app.route('/delete_f_user/<int:id>')
def delete_f_user(id):
    FUser.query.filter_by(id_f_user=id).delete()
    db.session.commit()
    return redirect(url_for('f_users'))

@app.route('/download_csv_f_users')
def download_csv_f_users():
    libelle_famille = session['libelle_famille']
    coefficient = session['coefficient']
    remarques = session['remarques']
    users = FUser.query.filter(
            and_(
                FUser.libelle_famille.like(f"%{libelle_famille}%"),
                FUser.coefficient.like(f'%{coefficient}%'),
                FUser.remarques.like(f'%{remarques}%')
            )
        ).all()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Libelle Famille', 'Coefficient', 'Remarques'])
    for user in users:
        cw.writerow([user.id_f_user, user.libelle_famille, user.coefficient, user.remarques])
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=f_user_list.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

@app.route('/download_html_f_users')
def download_html_f_users():
    libelle_famille = session['libelle_famille']
    coefficient = session['coefficient']
    remarques = session['remarques']
    users = FUser.query.filter(
            and_(
                FUser.libelle_famille.like(f"%{libelle_famille}%"),
                FUser.coefficient.like(f'%{coefficient}%'),
                FUser.remarques.like(f'%{remarques}%')
            )
        ).all()
    html = render_template('f_users/f_user_list.html', users=users)
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = 'attachment; filename=f_user_list.html'
    return response