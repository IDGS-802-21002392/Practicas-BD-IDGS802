from flask import Flask, request, render_template, Response
import forms 
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g
from config import DevelopmentConfig
from models import db
from models import Alumnos
from models import Maestros

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf= CSRFProtect()

@app.route("/index", methods=["GET", "POST"])
def index():
    alum_form = forms.UserForm2(request.form)
    mae_form = forms.UserForm3(request.form)

    if request.method == 'POST':
        if alum_form.validate():  # Asumiendo que quieres validar y agregar solo si el formulario de alumno es válido
            alum = Alumnos(nombre=alum_form.nombre.data, apaterno=alum_form.apaterno.data,
                           email=alum_form.email.data)
            db.session.add(alum)  # Agrega el objeto alumno a la sesión de la base de datos
            
        if mae_form.validate():  # Similarmente, valida y agrega el maestro solo si su formulario es válido
            mae = Maestros(nombre=mae_form.nombre.data, apaterno=mae_form.apaterno.data,
                           amaterno=mae_form.amaterno.data, email=mae_form.email.data, materias=mae_form.materias.data)
            db.session.add(mae)  # Agrega el objeto maestro a la sesión de la base de datos

        db.session.commit()  # Commit una vez después de agregar todos los objetos necesarios

    # Corregir la llamada a render_template para usar nombres de argumento únicos
    return render_template("index.html", form =alum_form, form1=mae_form)


@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    mae_form = forms.UserForm3(request.form)
    maestro = Maestros.query.all()

    return render_template("ABC_Completo.html", alumno=alumno, maestro = maestro)

@app.route("/alumnos", methods=["GET", "POST"])
def index1():
    print('dentro de alumnos')
    valor = g.prueba
    print('El dato es: {}'.format(valor))
    nom=""
    email=""
    apaterno=""
    alum_form = forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        email=alum_form.email.data
        apaterno=alum_form.apaterno.data
        mensaje = 'Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre:{}".format(nom))
        print("email:{}".format(email))
        print("apellido:{}".format(apaterno))
    return render_template("alumnos.html", form= alum_form, nom=nom, email=email, apaterno=apaterno)

if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
