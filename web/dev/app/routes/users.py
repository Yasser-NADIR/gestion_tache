from flask import render_template, request, flash, redirect, url_for, make_response
from flask import current_app as app
from sqlalchemy import and_
from ..models import User
from ..forms import UserSearchForm, UserForm
from ..utils import find_libelle_fuser_by_id
from .. import db
import io
import csv

@app.route('/users', methods=['GET', 'POST'])
def users():
    users = User.query.all()
    search_form = UserSearchForm()
    if request.method == 'POST' and search_form.validate_on_submit():
        users = User.query.filter(
            and_(
                User.nom.like(f'%{search_form.nom.data}%'),
                User.age.like(f'%{search_form.age.data}%'),
                User.email.like(f'%{search_form.email.data}%'),
                User.id_f_user.like(f'%{search_form.id_f_user.data}%')
            )
        ).all()
    return render_template('users/users.html', users=users, search_form=search_form, libelle_famille=find_libelle_fuser_by_id)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if request.method=='POST' and form.validate_on_submit():
        new_user = User(
            nom=form.nom.data,
            age=form.age.data,
            email=form.email.data,
            id_f_user=form.id_f_user.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('users'))
    return render_template('users/add_user.html', form=form)

@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)
    form = UserForm(obj=user)
    if request.method=='POST' and form.validate_on_submit():
        user.nom=form.nom.data
        user.age=form.age.data
        user.email=form.email.data
        user.id_f_user=form.id_f_user.data
        db.session.commit()
        flash('User edited successfully!', 'success')
        return redirect(url_for('users'))
    return render_template('users/edit_user.html', form=form, user=user)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.query.filter_by(id_users=id).delete()
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/download_csv_users')
def download_csv_users():
    users = User.query.all()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Nom', 'Age', 'Email', 'Famille'])
    for user in users:
        cw.writerow([user.id_users, user.nom, user.age, find_libelle_fuser_by_id(user.id_f_user)])
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=user_list.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

@app.route('/download_html_users')
def download_html_users():
    users = User.query.all() 
    html = render_template('users/user_list.html', users=users, libelle_famille=find_libelle_fuser_by_id)
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = 'attachment; filename=user_list.html'
    return response