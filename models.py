from flask_sqlalchemy import SQLAlchemy
import datetime

db= SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

class Maestros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    amaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    materias = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    

class Pizzeria(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(11))
    total = db.Column(db.Float)
    create_date = db.Column(db.DateTime)
    #dia = db.Column(db.String(30))
    #mes = db.Column(db.String(30))
    #anio=db.Column(db.Integer)
