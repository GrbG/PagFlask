#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import forms  # archivo forms

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    coment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and coment_form.validate():
        print(coment_form.username.data)
        print(coment_form.email.data)
        print(coment_form.comment.data)
    titulo = 'Curso Flask.'
    return render_template('index.html', title=titulo, form=coment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
