from flask import render_template, request, redirect, url_for, make_response, session
from flask import current_app as app
from sqlalchemy import and_
from ..models import Tache
from ..forms import TacheSearchForm, TacheForm
from .. import db
from datetime import datetime
from xhtml2pdf import pisa
import io
import csv


@app.route('/taches', methods=['GET', 'POST'])
def taches():
    taches = Tache.query.all()
    search_form = TacheSearchForm()
    session['libelle_tache'] = ''
    session['coefficient'] = ''
    session['remarques'] = ''
    if request.method == 'POST' and search_form.validate_on_submit():
        session['tache_tache'] = search_form.libelle_tache.data
        session['coefficient'] = search_form.coefficient.data
        session['remarques'] = search_form.remarques.data
        taches = Tache.query.filter(
            and_(
                Tache.libelle_tache.like(f'%{search_form.libelle_tache.data}%'),
                Tache.coefficient.like(f'%{search_form.coefficient.data}%'),
                Tache.remarques.like(f'%{search_form.remarques.data}%')
            )
        ).all()
    return render_template('taches/taches.html', taches=taches, search_form=search_form)

@app.route('/add_tache', methods=['GET', 'POST'])
def add_tache():
    form = TacheForm()
    if request.method =='POST' and form.validate_on_submit():
        new_tache = Tache(
            libelle_tache=form.libelle_tache.data,
            coefficient=form.coefficient.data,
            remarques=form.remarques.data
        )
        db.session.add(new_tache)
        db.session.commit()
        return redirect(url_for('taches'))
    return render_template('taches/add_tache.html', form=form)

@app.route('/edit_tache/<int:id>', methods=['GET', 'POST'])
def edit_tache(id):
    tache = Tache.query.get(id)
    form = TacheForm(obj=tache)
    if request.method == 'POST' and form.validate_on_submit():
        tache.libelle_tache = form.libelle_tache.data
        tache.coefficient = form.coefficient.data
        tache.remarques = form.remarques.data
        db.session.commit()
        return redirect(url_for('taches'))
    return render_template('taches/edit_tache.html', tache=tache, form=form)

@app.route('/delete_tache/<int:id>')
def delete_tache(id):
    Tache.query.filter_by(id_tache=id).delete()
    db.session.commit()
    return redirect(url_for('taches'))

@app.route('/download_csv_tache')
def download_csv_tache():
    Taches = Tache.query.all()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Libelle Tache', 'Coefficient', 'Remarques'])
    for tache in Taches:
        cw.writerow([tache.id_tache, tache.libelle_tache, tache.coefficient, tache.remarques])
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=tache_list.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

@app.route('/download_html_tache')
def download_html_tache():
    taches = Tache.query.all()
    html = render_template('taches/tache_list.html', taches=taches)
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Content-Disposition'] = 'attachment; filename=tache_list.html'
    return response


@app.route('/download_pdf_tache/<int:id>')
def download_pdf_tache(id):
    tache = Tache.query.get(id)
    now = str(datetime.now().date())
    html = render_template('taches/tache_pdf.html', tache=tache, now=now)
    pdf_buffer = io.BytesIO()
    pisa.CreatePDF(html, pdf_buffer)
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Type'] = 'text/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=tache {tache.libelle_tache}.pdf'
    return response

@app.route('/download_pdf_list_tache')
def download_pdf_list_tache():
    libelle_tache = session['libelle_tache']
    coefficient = session['coefficient']
    remarques = session['remarques']
    taches = Tache.query.filter(
            and_(
                Tache.libelle_tache.like(f"%{libelle_tache}%"),
                Tache.coefficient.like(f'%{coefficient}%'),
                Tache.remarques.like(f'%{remarques}%')
            )
        ).all()
    current_date = str(datetime.now().date())
    html = render_template('taches/tache_list_pdf.html', taches=taches, current_date=current_date)
    pdf_buffer = io.BytesIO()
    pisa.CreatePDF(html, pdf_buffer)
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Type'] = 'text/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=taches.pdf'
    return response