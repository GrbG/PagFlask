#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response
from flask import session, redirect, url_for, flash, g
from flask_wtf import CSRFProtect
import forms  # archivo forms
import json

from config import DevelopmentConfig
from models import db, User, Comment


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for('login'))
    elif 'username' in session and request.endpoint in ['login', 'create']:
        return redirect(url_for('index'))


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
    titulo = 'Index'
    return render_template('index.html', title=titulo)


@app.after_request
def after_request(response):
    return response  # siempre se debe retornar para mostrar la pag


@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'alvaro')
    return response


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = 'Login'
    login_form = forms.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()

        if user is not None:  # and User.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o Password No Valido'
            flash(error_message)

        session['username'] = login_form.username.data
    return render_template('login.html', title=login, form=login_form)


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    titulo = 'Curso Flask.'
    coment_form = forms.CommentForm(request.form)
    user_id = session['user_id']
    print('user id dentro del validate:', user_id)
    print('uno:', request.method)
    print('comentario:', coment_form.comment.data)
    if request.method == 'POST' and coment_form.validate():
        comment = Comment(user_id=user_id, text=coment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
        success_message = 'Nuevo Comentario Enviado'
        flash(success_message)
    else:
        pass
    return render_template('comment.html', title=titulo, form=coment_form)


# @app.route('/ajax-login', methods=['POST'])
# def ajax_login():
#     username = request.form['username']
#     response = {'status': 200, 'username': username, 'id': 1}
#     return json.dumps(response)


@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(create_form.username.data,
                    create_form.email.data,
                    create_form.password.data)
        db.session.add(user)  # me conecto y quedo conectado en la bd
        db.session.commit()  # transacción
        success_message = 'Usuario Encontrado en la BD'
        flash(success_message)
    return render_template('create.html', form=create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)  # inicio la conexion a la bd
    with app.app_context():
        db.create_all()  # creo las tablas
    app.run(port=8000)
# debug=True es para que el servidor siempre este escuchando nuevos cambios
# esta en el archivo de config
