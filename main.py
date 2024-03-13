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
from datetime import datetime
import os
from sqlalchemy import extract, func


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

id=0

@app.route("/pizzas", methods=["GET", "POST"])
def pizzasAgregar():
    form = forms.UserForm4(request.form)
    nombre = ""
    direccion = ""
    telefono = ""
    fechaRegistro=""
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
    ventas_Dia=0
    tabla_ventas=[]
    suma_ventas=[]
    if request.method == 'POST':
        if 'Agregar' in request.form:
            
            tamanio = form.tamanio.data
            pinia = form.pinia.data
            champinion=form.champinion.data
            jamon= form.jamon.data
            numPizza = form.numPizzas.data
            subTotal = calcular(tamanio, pinia, champinion, jamon, numPizza)
            agregar(tamanio, pinia, champinion, jamon, numPizza, subTotal)
            
            with open('registroPizzeria.txt', 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) >= 7:
                        id, tamanio, pinia, champinion, jamon, num_pizzas, subtotal = data
                        pizza = {'id': id, 'tamanio': tamanio, 'num_pizzas': num_pizzas, 'subtotal': subtotal}
                        if pinia =='True':
                            pizza['pinia'] = pinia
                        if champinion =='True':
                            pizza['champinion'] = champinion
                        if jamon =='True':
                            pizza['jamon'] = jamon
                        pizzas.append(pizza)
                    else:
                        print(f"La línea '{line}' no tiene suficientes elementos")
        elif 'Quitar' in request.form:
            with open("registroPizzeria.txt", "r", encoding="utf-8") as file:
                lineas = file.readlines()
 
            id_omitir = int(request.form['Quitar'])  # Cambiar según el ID a omitir

            #with open("registroPizzeria.txt", "r", encoding="utf-8") as file:
            #    lineas = file.readlines()

            with open("registroPizzeria.txt", "w", encoding="utf-8") as file:
                for linea in lineas:
                    # Separamos la línea por comas, asumiendo que el primer elemento es el ID
                    partes = linea.strip().split(',')
                    # Convertimos el primer elemento a entero y lo comparamos con el ID a omitir
                    pedido_id = int(partes[0])  # Convertimos el ID de string a int
                    if pedido_id != id_omitir:
                        # Si el ID no es el que queremos omitir, escribimos la línea en el archivo
                        file.write(linea)
            pedidos_formateados = []
            print(pedidos_formateados)

            with open("registroPizzeria.txt", "r", encoding="utf-8") as file:
                lineas = file.readlines()
                
            totalBD = 0.0

            with open("registroPizzeria.txt", "r", encoding="utf-8") as file:
                pedidos = file.readlines()

            for pedido in pedidos:
                partes = pedido.strip().split(',')
                subtotal = float(partes[-1])
                totalBD += subtotal

            print("TotalBD:", totalBD)

            with open('registroPizzeria.txt', 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) >= 7:
                        id, tamanio, pinia, champinion, jamon, num_pizzas, subtotal = data
                        pizza = {'id': id, 'tamanio': tamanio, 'num_pizzas': num_pizzas, 'subtotal': subtotal}
                        if pinia =='True':
                            pizza['pinia'] = pinia
                        if champinion =='True':
                            pizza['champinion'] = champinion
                        if jamon =='True':
                            pizza['jamon'] = jamon
                        pizzas.append(pizza)
                    else:
                        print(f"La línea '{line}' no tiene suficientes elementos")
                
                
        elif 'Terminar' in request.form:
            print("terminar")
            tamanio = form.tamanio.data
            pinia = form.pinia.data
            champinion=form.champinion.data
            jamon= form.jamon.data
            numPizza = form.numPizzas.data
            direccion=form.direccion.data
            telefono = form.telefono.data
            fechaRegistro =form.fechaRegistro.data
            subTotal = calcular(tamanio, pinia, champinion, jamon, numPizza)
            pizz = Pizzeria(nombre=form.nombre.data, total=subTotal, direccion=form.direccion.data, telefono = form.telefono.data, create_date=fechaRegistro)
            db.session.add(pizz)
            db.session.commit()
            ventas_Dia = sumar_ventas_hoy()
            fecha_actual=datetime.now()
            pizza= Pizzeria.query.filter(
                Pizzeria.create_date.like(f"{fecha_actual.year}-{fecha_actual.month:02d}-{fecha_actual.day:02d}%")
            ).all()
            os.remove('registroPizzeria.txt')
            os.system('touch registroPizzeria.txt')
            form.telefono.data=None
            form.numPizzas.data=None
            form.process()
            return render_template('indexPizza.html', form=form, pizza=pizza, ventas_Dia=ventas_Dia)
        elif 'fecha' in request.form:
            try:
                fecha_input = request.form['fecha']
                tabla_ventas = ventas_por_fecha(fecha_input)
                suma_ventas = sum(venta[1] for venta in tabla_ventas)
                print("Total de ventas:", suma_ventas)
            except Exception as e:
                print(f"Error al procesar la fecha: {e}")
    return render_template('indexPizza.html', form=form,suma_ventas=suma_ventas, tabla_ventas=tabla_ventas, fechaRegistro=fechaRegistro, ventas_Dia=ventas_Dia, pizza=pizza, total=total, pizzas=pizzas, nombre=nombre, tamanio=tamanio, pinia=pinia, champinion=champinion, jamon=jamon, numPizza=numPizza, subTotal=subTotal, archivo=archivo, direccion=direccion, telefono=telefono)

def ventas_por_fecha(fecha):
    # Diccionarios de días de la semana y meses
    dias = {
        0: "domingo",
        1: "lunes",
        2: "martes",
        3: "miercoles",
        4: "jueves",
        5: "viernes",
        6: "sabado"
    }
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }

    # Convertir 'fecha' a minúsculas para hacer la comparación
    fecha = fecha.lower()

    try:
        if fecha in dias.values():
            # Obtener el número correspondiente al día de la semana
            dia_semana = list(dias.keys())[list(dias.values()).index(fecha)]
            # Filtrar por el número del día de la semana
            ventas = Pizzeria.query.filter(db.func.DAYOFWEEK(Pizzeria.create_date) == dia_semana + 1).all()
            
        elif fecha in meses.values():
            # Obtener el número correspondiente al mes
            mes = list(meses.keys())[list(meses.values()).index(fecha)]
            # Filtrar por el número del mes
            ventas = Pizzeria.query.filter(extract('month', Pizzeria.create_date) == mes).all()
            
        else:
            print("Fecha no válida. Debe ser un día de la semana o un mes.")
            return []

        if not ventas:
            print(f"No se encontraron ventas para la fecha: {fecha}")
            return []
        
        # Crear una lista de tuplas con los datos de las ventas
        
        tabla_ventas = [(venta.nombre, venta.total, venta.create_date) for venta in ventas]


    except Exception as e:
        print(f"Error al obtener las ventas: {e}")
        tabla_ventas = []  # En caso de error, devolver una lista vacía

    
    return tabla_ventas

def sumar_ventas_hoy():
    fecha_actual = datetime.now()
    ventas_del_dia = Pizzeria.query.filter(
        #Pizzeria.create_date.like(f"{fecha_actual.year}-{fecha_actual.month:02d}-{fecha_actual.day:02d}%")
        Pizzeria.create_date.like(f"{fecha_actual.year}-{fecha_actual.month:02d}-{fecha_actual.day:02d}%")
    ).all()
    total_ventas = sum(venta.total for venta in ventas_del_dia)
    print(total_ventas)
    return total_ventas

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
    global id
    id += 1
    with open('registroPizzeria.txt', 'a') as f:
        f.write(f'{id},{tamanio},{pinia},{champinion},{jamon},{numPizza},{subTotal}\n')


if __name__ =="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
