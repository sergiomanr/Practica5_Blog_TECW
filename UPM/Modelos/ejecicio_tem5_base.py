import csv
from flask import Flask
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists


app = Flask(__name__)
url = 'postgresql://postgres:12345@localhost:5432/basedatos'
app.config['SQLALCHEMY_DATABASE_URI'] = url

if not database_exists(url):
    create_database(url)

db = SQLAlchemy(app)


class Equipo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sede = db.Column(db.String,nullable=False)
    nombre = db.Column(db.String)

juega = db.Table('juega',
    db.Column('jugador_id',db.Integer,db.ForeignKey('jugador.id'),primary_key=True),
    db.Column('partido_id',db.Integer, db.ForeignKey('partido.id'),primary_key= True))


class jugador(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sede = db.Column(db.String,nullable=False)
    posicion = db.Column(db.String)
    numero = db.Column(db.Integer)
    goles = db.Column(db.Integer)
    id_equipo = db.Column(db.String,db.ForeignKey('equipo.id'))
    partidos = db.relationship('partido',secondary=juega,backref='jugadores')

class partido(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fecha = db.Column(db.Date)
    jugadores = db.relationship('jugador', secondary=juega, backref='partidos')

query = db.Select(Equipo).where(Equipo.sede=='Madrid')
equipos = db.session.execute(query).all()
equipos = [id for id, in equipos]

query = db.Select(partido).join(juega.partido_id).where(jugador_id=10)
partidos = db.execute(query).all()
partidos = [id for id, in partidos]

query = db.Select(jugador).where(jugador.id==35)
jugador = db.session.execute(query).first()[0]
jugador.numero= 10
jugador.goles = 25
db.session.commit()