from wtforms import Form, validators
from wtforms import StringField, TextField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField
from models import User


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El Campo debe estar vacio')


class CommentForm(Form):
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

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise validators.ValidationError('El usuario ya existe')
