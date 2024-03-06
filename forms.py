from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField, SelectMultipleField, BooleanField
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

class UserForm4 (Form):
    #id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField("nombre", [
        validators.Length(min=4, max=35, message='ingrese un nombre valido')
    ])
    direccion = StringField('direccion', [validators.Length(min=4, max=35,message='ingrese una direccion valida')])
    telefono = IntegerField('telefono',  [validators.Length(min=10, max=10,message='ingrese un telefono valida')])
    tamanio = RadioField('tamanio', choices=[
    ('Chica', 'Chica $40'),
    ('Mediana', 'Mediana $80'),
    ('Grande', 'Grande $120')])

    jamon = BooleanField('Jamon $10', default=False)
    pinia = BooleanField('Piña $10', default=False)
    champinion=BooleanField('Champiñones $10', default=False)
    numPizzas = IntegerField('numPizzas', [validators.Length(min=1, max=2,message='ingrese el numeor de pizzas')])

