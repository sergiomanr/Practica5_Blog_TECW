import csv
from flask import Flask
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from collections import defaultdict
import psycopg2

app = Flask(__name__)
url = 'postgresql://postgres:12345@localhost:5432/basedatos'
app.config['SQLALCHEMY_DATABASE_URI'] = url

if not database_exists(url):
    create_database(url)

db = SQLAlchemy(app)

class Libros(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    edition_Statement = db.Column(db.String)
    place = db.Column(db.String)
    date = db.Column(db.Integer)
    publisher = db.Column(db.String)
    title = db.Column(db.String)
    author = db.Column(db.String)
    contributors = db.Column(db.String)
    corporate_author = db.Column(db.String)
    corporate_contributors = db.Column(db.String)
    former_owner=db.Column(db.String)
    engraver=db.Column(db.String)
    issuance_type=db.Column(db.String)
    flickr_URL=db.Column(db.String)
    shelfmarks=db.Column(db.String)

    def __init__(self, id, edition_Statement, place,date,
                 publisher,title,author,contributors,corporate_author,corporate_contributors
                 ,former_owner,engraver,issuance_type,flickr_URL,shelfmarks):
        
        self.id = id
        self.edition_Statement = edition_Statement
        self.place = place
        self.date = date
        self.publisher = publisher
        self.title = title
        self.author = author
        self.contributors = contributors
        self.corporate_author = corporate_author
        self.corporate_contributors = corporate_contributors
        self.former_owner = former_owner
        self.engraver = engraver
        self.issuance_type = issuance_type
        self.flickr_URL = flickr_URL
        self.shelfmarks = shelfmarks

app.app_context().push()
db.create_all()



def filtro_fecha(fecha):
    regex = r'^(\d{4})'
    try:
        finds = re.findall(regex,str(fecha))
        if len(finds)>0:
            return int(finds[0])
        return None
    except:
        return None

def filtro_cuidad(lugar):
    regex = r"^[A-Z][a-zA-Z]+[^a-zA-Z]?"
    finds = re.findall(regex,str(lugar))
    if lugar.isdigit():
        return None
    else:
        try:
            for i in finds:
                if i[-1] in r',|;|)|]|(|[':
                    return i[:-1]
            else:
                return lugar
        except:
            return None
    
def filtro_shelfmark(shelf):
    regex = r'(\d{4,6}\.\w{1,3}\.\d{1,2})'
    try:
        finds = re.findall(regex,str(shelf))
        if len(finds)>0:
            return finds[0]
        return None
    except:
        return None

def filtro_publisher(publi):
    try:
        finds = re.findall(r'published by (.*)',publi)
        if finds:
            return finds[0]
        else:
            return publi
    except:
        return None

def filtro_edicion(edic):
    try:
        if edic.startswith('A new') or edic.startswith('New'):
            return 'New edition'
        elif edic.startswith('[') or edic.startswith('('):
            palabra = ''
            tipo = edic.split()[0]
            edicion = edic.split()[1]
            if tipo[0] in r']|[|(|)':
                palabra += tipo[1:]+' '
            if edicion[-1] in r']|[|(|)':
                palabra += edicion[:-2]
            return palabra
        else:
            return edic.split()[0]+' '+edic.split()[1][:-1]
    except:
        return None    
    
with open('./base/libros_10.csv',mode='r',encoding='utf8') as fishe:
    next(fishe)
    for i in csv.reader(fishe):
        id = i[0]
        edition = filtro_edicion(i[1])
        place = filtro_cuidad(i[2])
        date = filtro_fecha(i[3])
        publisher = filtro_publisher(i[4])
        title = i[5] 
        author = i[6]
        contributors = i[7]
        corporate_author = i[8]
        corporate_contributors = i[9]
        former_owner = i[10]
        engraver = i[11]
        issuance_type = i[12]
        flickr_URL = i[13]
        shelfmark = filtro_shelfmark(i[14])
        new_libro = Libros(id,edition,place,date,publisher,title,author,contributors,
                           corporate_author,corporate_contributors,former_owner,engraver,
                           issuance_type,flickr_URL,shelfmark)
        db.session.add(new_libro)
        db.session.commit()



query = db.select(Libros).where(Libros.date >= 1850, Libros.date <= 1859)
libros = db.session.execute(query)
print(len(libros.all()))




