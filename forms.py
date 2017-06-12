from wtforms import Form, validators
from wtforms import StringField, TextField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El Campo debe estar vacio')


class CommentForm(Form):
    username = StringField('Nombre Usuario',
                           [
                               validators.Required(
                                   message='El Campo es Obligatorio'),
                               validators.length(
                                   min=4, max=25,
                                   message='Ingrese un \
                                   Usuario Valido!(4 a 25 caracteres).'),
                           ])
    email = EmailField('Correo Electronico',
                       [
                           validators.Required(
                               message='El Campo es Obligatorio'),
                           validators.Email(
                               message='Ingrese un Formato Valido')
                       ])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])


class LoginForm(Form):
    username = StringField('Username',
                           [
                               validators.Required(
                                   message='Campo Obligatorio'),
                               validators.length(
                                   min=4, max=25,
                                   message='Ingrese un Usuario Valido'),
                           ])
    password = PasswordField('Password',
                             [
                                 validators.Required(
                                     message='Campo Obligatorio')
                             ])


class CreateForm(Form):
    username = TextField('Username',
                         [
                             validators.Required(
                                 message='El user es Obligatorio'),
                             validators.length(
                                 min=4, max=50,
                                 message='Ingrese un user valido')
                         ])
    email = EmailField('Correo Electronico',
                       [
                           validators.Required(
                               message='El email es requerido'),
                           validators.Email(message='Ingrese un Mail'),
                           validators.length(
                               min=4, max=50,
                               message='Ingrese un correo valido')
                       ])
    password = PasswordField('Contraseña',
                             [
                                 validators.Required(
                                     message='El password es obligatorio')
                             ])
