from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, IntegerField, SearchField, BooleanField, DateField
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
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField("nombre", [
        validators.Length(min=4, max=35, message='ingrese un nombre valido')
    ])
    fechaRegistro = DateField('Fecha de Registro', format='%Y-%m-%d')
    #dia = SelectField('dia', choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('domingo', 'Domingo')], validators=[validators.DataRequired(message="El campo es requerido")])
    #mes = SelectField('mes', choices=[('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril', 'Abril'), ('mayo', 'Mayo'), ('junio', 'Junio'), ('julio', 'Julio'), ('agosto', 'Agosto'), ('septiembre', 'Septiembre'), ('octubre', 'Octubre'), ('noviembre', 'Noviembre'), ('diciembre', 'Diciembre')], validators=[validators.DataRequired(message="El campo es requerido")])
    #anio = IntegerField('año', [validators.number_range(min=1900, max=2024, message='valor no valido')])
    direccion = StringField('direccion', [validators.Length(min=4, max=35,message='ingrese una direccion valida')])
    telefono = IntegerField('telefono',  [validators.Length(min=10, max=10,message='ingrese un telefono valida')])
    tamanio = RadioField('tamanio', choices=[
    ('Chica', 'Chica $40'),
    ('Mediana', 'Mediana $80'),
    ('Grande', 'Grande $120')])
    jamon = BooleanField('Jamon $10', default=False)
    pinia = BooleanField('Piña $10', default=False)
    champinion=BooleanField('Champiñones $10', default=False)
    numPizzas = IntegerField('numPizzas', [validators.number_range(min=1, max=20,message='ingrese el numero de pizzas')])

