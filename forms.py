from wtforms import Form, validators
from wtforms import StringField, TextField, HiddenField
from wtforms.fields.html5 import EmailField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El Campo debe estar vacio')


class CommentForm(Form):
    username = StringField('Nombre Usuario',
                           [
                               validators.required(
                                   message='El Campo es Obligatorio'),
                               validators.length(
                                   min=4, max=25,
                                   message='Ingrese un \
                                   Usuario Valido!(4 a 25 caracteres).'),
                           ])
    email = EmailField('Correo Electronico',
                       [
                           validators.required(
                               message='El Campo es Obligatorio'),
                           validators.Email(
                               message='Ingrese un Formato Valido')
                       ])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])
