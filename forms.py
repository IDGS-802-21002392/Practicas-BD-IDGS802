from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField
from wtforms import EmailField 
from wtforms import validators

class UserForm2 (Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField("nombre", [
        validators.DataRequired(message='campo es requerido'), 
        validators.length(min=4, max=10, message='ingrese un nombre valido')
    ])
    email = EmailField('correo', [validators.Email(message='ingrese un correo valido')])
    apaterno = StringField('apaterno')

class UserForm3 (Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField("nombre", [
        validators.DataRequired(message='campo es requerido'), 
        validators.Length(min=4, max=10, message='ingrese un nombre valido')
    ])
    email = EmailField('correo', [validators.Email(message='ingrese un correo valido')])
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    materias = StringField('materias')

