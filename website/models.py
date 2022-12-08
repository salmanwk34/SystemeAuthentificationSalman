# Importation du fichier db.py
from . import db
# Importation de la classe UserMixin 
from flask_login import UserMixin
# Importation de la fonction func 
from sqlalchemy.sql import func 

# Creation de la classe Note qui herite de la classe Model de SQLAlchemy
class Note(db.Model): 
    # Creation de la colonne id
    id = db.Column(db.Integer, primary_key=True) 
    # Creation de la colonne data
    data = db.Column(db.String(10000))
    # Creation de la colonne date 
    date = db.Column(db.DateTime(timezone=True), default=db.func.now())
    # Creation de la colonne user_id  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

# Creation de la classe User
class User(db.Model, UserMixin):
    # Creation de la colonne id 
    id = db.Column(db.Integer, primary_key=True)
    # Creation de la colonne email 
    email = db.Column(db.String(150), unique=True)
    # Creation de la colonne password 
    password = db.Column(db.String(150))
    # Creation de la colonne first_name 
    first_name = db.Column(db.String(150))
    # Creation de la relation entre la table Note et la table User 
    notes = db.relationship('Note') 
