# Importation de la classe Blueprint
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Importation des classes User et Note du fichier models.py                                                
from .models import User
# Importation de la fonction generate_password_hash  
from werkzeug.security import generate_password_hash, check_password_hash
# Importation de db  
from . import db 
# Importation des fonctions login_user, login_required, logout_user et current_user
from flask_login import login_user, login_required, logout_user, current_user 

# Creation du blueprint auth
auth = Blueprint('auth', __name__) 

# Route de la page de connexion + requetes 
@auth.route('/Connexion', methods=['GET', 'POST']) 
# Fonction de la page de connexion
def login(): 
    # Si la requete est POST
    if request.method == 'POST':
        # Recuperation de l'email 
        email = request.form.get('email')
        # Recuperation du mot de passe
        password = request.form.get('password') 
        # Recuperation de l'utilisateur
        user = User.query.filter_by(email=email).first() 
        # Si l'utilisateur existe
        if user:
            # Si le mot de passe est correct
            if check_password_hash(user.password, password):
                # Message de succes 
                flash('Connexion reussie', category='success')
                # Connexion de l'utilisateur 
                login_user(user, remember=True)
                # Redirection vers la page d'accueil 
                return redirect(url_for('views.home'))
            # Si le mot de passe est incorrect 
            else:
                # Message d'erreur
                flash('Mot de passe incorrect', category='error') 
        # Si l'utilisateur n'existe pas
        else: 
            # Message d'erreur
            flash('Utilisateur inexistant', category='error') 
    # Retourne le code HTML de la page de connexion + l'utilisateur
    return render_template("login.html", user=current_user) 

# Route de la page de deconnexion          
@auth.route('/Deconnexion')
# Fonction de la page de deconnexion 
@login_required 
def logout():
    # Deconnexion de l'utilisateur 
    logout_user() 
    # Redirection vers la page de connexion
    return redirect(url_for('auth.login')) 
    
# Route de la page d'inscription
@auth.route('/Inscription', methods=['GET', 'POST'])
# Fonction de la page d'inscription 
def sign_up():
    # Si la requete est POST
    if request.method == 'POST': 
        # Recuperation de l'email
        email = request.form.get('email')
        # Recuperation du prenom  
        first_name = request.form.get('firstname')
        # Recuperation du mot de passe 1
        password1 = request.form.get('password1')
        # Recuperation du mot de passe 2  
        password2 = request.form.get('password2') 

        user = User.query.filter_by(email=email).first()
        # Si l'utilisateur existe 
        if user: 
            flash('Utilisateur deja existant', category='error')
        # Si l'email est trop court
        elif len(email) < 4: 
            flash('Email trop court', category='error')
        # Si le prenom est inferieur a 2 caracteres
        elif len(first_name) < 2:
            # Affichage d'un message d'erreur
            flash('Prenom doit contenir au moins 2 caracteres.', category='error') 
        # Si l'email est inferieur a 4 caracteres
        elif len(email) < 4:
            # Affichage d'un message d'erreur
            flash('Email doit contenir au moins 4 caracteres.', category='error') 
        # Si les mots de passe ne sont pas identiques    
        elif password1 != password2:
            # Affichage d'un message d'erreur 
            flash('Les mots de passe ne correspondent pas.', category='error') 
        # Si le mot de passe est inferieur a 7 caracteres    
        elif len(password1) < 7:
            # Affichage d'un message d'erreur
            flash('Mot de passe doit contenir au moins 7 caracteres.', category='error')  
        # Si tout est bon
        else:
            # Creation d'un nouvel utilisateur  
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Ajout de l'utilisateur a la base de donnees 
            db.session.add(new_user) 
            # Sauvegarde des donnees dans la base de donnees   
            db.session.commit()
            # Affichage d'un message de succes   
            flash("Compte cree!", category='success')
            # Redirection vers la page d'accueil
            return redirect(url_for('views.home')) 
    # Retourne le code HTML de la page d'inscription + l'utilisateur
    return render_template("sign_up.html", user=current_user) 




        
