from flask import Flask, request, render_template, Response
import forms 
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g
from config import DevelopmentConfig
from models import db
from models import Alumnos
from models import Maestros
from models import Pizzeria
import os

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

@app.route("/pizzas", methods=["GET", "POST"])
def pizzasAgregar():
    form = forms.UserForm4(request.form)
    nombre = ""
    direccion = ""
    telefono = ""
    tamanio = ""
    jamon=""
    pinia=""
    champinion=""
    numPizza = ""
    subTotal = ""
    archivo = ""
    total = ""
    pizzas=[]
    pizza=""

    if request.method == 'POST' and 'submit' in request.form:
        if request.form['submit'] == 'Agregar':
            tamanio = form.tamanio.data
            pinia = form.pinia.data
            champinion=form.champinion.data
            jamon= form.jamon.data
            numPizza = form.numPizzas.data
            subTotal = calcular(tamanio, pinia, champinion, jamon, numPizza)
            agregar(tamanio, pinia, champinion, jamon, numPizza, subTotal)
            pizz = Pizzeria(nombre=form.nombre.data, total=subTotal)
            db.session.add(pizz)
            db.session.commit()
            pizza= Pizzeria.query.all()
            
            with open('registroPizzeria.txt', 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) >= 6:
                        tamanio, pinia, champinion, jamon, num_pizzas, subtotal = data
                        pizzas.append({'tamanio': tamanio, 'pinia': pinia, 'champinion':champinion, 'jamon':jamon, 'num_pizzas': num_pizzas, 'subtotal': subtotal})
                    else:
                        print(f"La línea '{line}' no tiene suficientes elementos")
        elif request.form['submit'] == 'Quitar':
            id = request.form.get("id")
            if id:
                with open('registroPizzeria.txt', 'r') as f:
                    lines = f.readlines()

                with open('registroPizzeria.txt', 'w') as f:
                    for line in lines:
                        if not line.startswith(str(id)):
                            f.write(line)

    return render_template('indexPizza.html', form=form, pizza=pizza, total=total, pizzas=pizzas, nombre=nombre, tamanio=tamanio, pinia=pinia, champinion=champinion, jamon=jamon, numPizza=numPizza, subTotal=subTotal, archivo=archivo, direccion=direccion, telefono=telefono)

def calcular(tamanio, pinia, champinion, jamon, numPizza):
    
    total = 0
    size_price = {"Chica": 40, "Mediana": 80, "Grande": 120}
    ingredient_price = {"Jamon": 10, "Piña": 10, "Champiñon": 10}

    base_price = size_price.get(tamanio, 0)
    total = base_price

    if pinia is not False:
        total += 10
    if champinion is not False:
        total += 10
    if jamon is not False:
        total += 10

    total *= numPizza

    return total

def agregar(tamanio, pinia, champinion, jamon, numPizza, subTotal):
    with open('registroPizzeria.txt', 'a') as f:
        f.write(f'{tamanio},{pinia},{champinion},{jamon},{numPizza},{subTotal}\n')

if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
