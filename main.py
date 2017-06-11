#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import forms  # archivo forms

app = Flask(__name__)


@app.route('/')
def index():
    coment_form = forms.CommentForm()
    titulo = 'Curso Flask.'
    return render_template('index.html', title=titulo, form=coment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
