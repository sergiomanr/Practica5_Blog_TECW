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

def filtro_edition(atr):
    if len(str)==1:
        return str
    else:
        return None
def filtro_fecha(fecha):
    
        return None
with open('libros_10.csv',mode='r',encoding='utf8') as fishe:
    for i in csv.reader(fishe):
        id = i[0]
        date = filtro_fecha(i[3])
        # palce = clean_place()
        # publisher = 
        # author = 
        # title = clean_title()
        # sejglfshark = cleanshelfmark()
        print(date)


class Libros(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    Edition_Statement = db.Column(db.String, nullable=False)
    Place_of_Publication = db.Column(db.String)
    Date_of_Publication = db.Column(db.Integer)
    Publisher = db.Column(db.String)
    Title = db.Column(db.String)
    Author = db.Column(db.String)
    Contributors = db.Column(db.String)
    Corporate_Author = db.Column(db.String)
    Corporate_Contributors = db.Column(db.String)
    Former_owner=db.Column(db.String)
    Engraver=db.Column(db.String)
    Issuance_type=db.Column(db.String)
    Flickr_URL=db.Column(db.String)
    Shelfmarks=db.Column(db.String)


with app.app_context():
    db.create_all()