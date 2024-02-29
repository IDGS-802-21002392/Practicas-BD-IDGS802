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
    alum_form=forms.UserForm2(request.form)
    if request.method=='POST' and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data, apaterno = alum_form.apaterno.data,
                 email = alum_form.email.data)
        #insert into alumnos values()
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=alum_form)

@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABCCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()

    return render_template("ABC_Completo.html", Alumnos=alumno)

@app.route("/index1", methods=["GET", "POST"])
def maestro():
    mae_form=forms.UserForm3(request.form)
    if request.method=='POST' and mae_form.validate():
        mae=Maestros(nombre=mae_form.nombre.data, apaterno = mae_form.apaterno.data, amaterno=mae_form.amaterno.data,
                 email = mae_form.email.data, materias = mae_form.materias.data)
        db.session.add(mae)
        db.session.commit()
    return render_template("index1.html", form=mae_form)

@app.route("/ABC_Completo1", methods=["GET", "POST"])
def ABCCompleto1():
    maestro = Maestros.query.all()

    return render_template("ABC_Completo1.html", Maestros=maestro)

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
