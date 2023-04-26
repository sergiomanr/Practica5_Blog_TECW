from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

app = Flask(__name__)
url = 'postgresql://postgres:12345@localhost:5432/Practica_bases'
app.config['SQLALCHEMY_DATABASE_URI'] = url

if not database_exists(url):
    create_database(url)

db = SQLAlchemy(app)

