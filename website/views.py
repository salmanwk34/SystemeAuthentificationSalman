# Importation de la classe Blueprint, de la fonction render_template, de la fonction request, de la fonction flash, de la fonction jsonify
from flask import Blueprint, render_template, request, flash, jsonify
# Importation de la fonction login_required et de la variable current_user 
from flask_login import login_required, current_user
# Importation de la classe Note du fichier models.py 
from .models import Note
# Importation du fichier db.py 
from . import db
# Importation du module json 
import json 


# Creation du blueprint views
views = Blueprint('views', __name__) 
# Route de la page d'accueil
@views.route('/', methods=['GET', 'POST'])
@login_required
# Fonction de la page d'accueil 
def home():
    # Si la requete est POST
    if request.method == 'POST':
        # Recuperation de la note 
        note = request.form.get('note') 
        # Si la note est vide
        if len(note) < 1: 
            # Message d'erreur
            flash('Note vide', category='error')
        # Si la note n'est pas vide 
        else:
            # Creation d'une nouvelle note
            new_note = Note(data=note, user_id=current_user.id) 
            # Ajout de la note a la base de donnees
            db.session.add(new_note)
            # Sauvegarde des modifications
            db.session.commit()
            # Message de succes
            flash('Note ajoute', category='success') 
    # Retourne le code HTML de la page d'accueil + l'utilisateur
    return render_template("home.html", user=current_user) 

# Route de la page de suppression de note
@views.route('/delete-note', methods=['POST'])
# Fonction de la page de suppression de note 
def delete_note():
    # Recuperation de la note 
    note = json.loads(request.data)
    # Recuperation de l'id de la note
    noteId = note['noteId']
    # Recuperation de la note
    note = Note.query.get(noteId)
    # Si la note existe 
    if note:
        # Si l'utilisateur est le proprietaire de la note
        if note.user_id == current_user.id: 
            # Suppression de la note
            db.session.delete(note)
            # Sauvegarde des modifications 
            db.session.commit()
    # Retourne un objet JSON vide         
    return jsonify({})
