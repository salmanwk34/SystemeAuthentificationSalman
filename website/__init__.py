# Importation de la classe Flask
from flask import Flask 
# Importation de la classe SQLAlchemy
from flask_sqlalchemy import SQLAlchemy 
# Importation de la fonction path
from os import path
# Importation de la classe LoginManager
from flask_login import LoginManager 
# Importation de la classe Blueprint, de la fonction render_template, de la fonction request, de la fonction flash, de la fonction redirect et de la fonction url_for
from flask import Blueprint, render_template, request, flash, redirect, url_for

# Creation de la base de donnees
db = SQLAlchemy() 
# Nom de la base de donnees
DB_NAME = "database.db" 

# Creation de fonction qui sera appelee dans le fichier main.py
def create_app():
    # Creation de l'application
    app = Flask(__name__)
    # Clé secrète pour la session 
    app.config['SECRET_KEY'] = 'zojeidjezidozeidze'
    # Chemin de la base de donnees 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialisation de la base de donnees 
    db.init_app(app) 

    # Importation du fichier views.py
    from .views import views
    # Importation du fichier auth.py 
    from .auth import auth 

    # Enregistrement du blueprint views
    app.register_blueprint(views, url_prefix='/') 
    # Enregistrement du blueprint auth
    app.register_blueprint(auth, url_prefix='/') 
    # Importation de la classe User et de la classe Note
    from .models import User, Note 
    # Creation de la base de donnees
    with app.app_context(): 
         db.create_all()
    
    # Creation de l'objet LoginManager     
    login_manager = LoginManager()
    # Redirection vers la page de connexion
    login_manager.login_view = 'auth.login'
    # Initialisation de l'objet LoginManager
    login_manager.init_app(app) 
    
    # Fonction qui permet de charger l'utilisateur
    @login_manager.user_loader 
    def load_user(id):
        # Retourne l'utilisateur
        return User.query.get(int(id)) 
    # Retourne l'application
    return app 

