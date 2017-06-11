#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response
from flask_wtf import CsrfProtect
import forms  # archivo forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # nadie deberia saber esto xd
csrf = CsrfProtect(app)


"""@app.route('/', methods=['GET', 'POST'])
def index():
    coment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and coment_form.validate():
        print(coment_form.username.data)
        print(coment_form.email.data)
        print(coment_form.comment.data)
    else:
        print('Error en el Formulario')

    titulo = 'Curso Flask.'
    return render_template('index.html', title=titulo, form=coment_form)
"""


@app.route('/')
def index():
    custom_cookie = request.cookies.get('custome_cookie', 'Undefined')
    print(custom_cookie)
    titulo = 'Index'
    return render_template('index.html', title=titulo)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    login = 'Login'
    return render_template('login.html', title=login, form=login_form)


@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'alvaro')
    return response


if __name__ == '__main__':
    app.run(debug=True, port=8000)
