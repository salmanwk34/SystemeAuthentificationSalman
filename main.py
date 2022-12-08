# Importation de la fonction create_app du fichier __init__.py
from website import create_app 

# Creation de l'application
app = create_app()
# Si le fichier est execute directement 
if __name__ == '__main__':
    # Lance l'application 
    app.run(debug=True) 
    