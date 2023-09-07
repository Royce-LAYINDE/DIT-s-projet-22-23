from flask import Flask, render_template, request, redirect, url_for
# Les imports ci-dessus permettent d'importer différentes fonctionnalités de Flask
# nécessaires pour la création d'une application web et la gestion des routes.

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# Les imports ci-dessus correspondent aux fonctionnalités de Flask-Login,
# un module qui facilite la gestion de l'authentification utilisateur.

import sqlite3
# L'import ci-dessus permet d'importer le module SQLite, qui fournit des fonctionnalités
# pour interagir avec des bases de données SQLite.

import bcrypt
# L'import ci-dessus permet d'importer le module Bcrypt, qui est utilisé pour le hachage
# sécurisé des mots de passe et la vérification des mots de passe hachés.



app = Flask(__name__)
# Création d'une instance de l'application Flask. __name__ est une variable spéciale qui
# contient le nom du module en cours d'exécution. Cela permet à Flask de savoir où se trouvent
# les ressources comme les modèles et les fichiers statiques.

app.secret_key = 'secret_key'  
# Configuration de la clé secrète de l'application. Cette clé est utilisée pour signer les cookies
# de session et d'autres éléments liés à la sécurité. Il est important de la garder confidentielle.

login_manager = LoginManager(app)
# Création d'une instance du gestionnaire de connexion (LoginManager). Cela permet à l'application
# de gérer les fonctionnalités liées à l'authentification et à la gestion des utilisateurs connectés.


# Définition de la classe User pour gérer les utilisateurs avec Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Chargement de l'utilisateur à partir de l'ID stocké dans la session
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Vérification des identifiants de l'utilisateur dans la base de données
def verify_credentials(email, password):
    conn = sqlite3.connect("C:/Users/Rab/Documents/DIT-s-projet-22-23/Projet/DIT_Projet.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, mot_de_passe FROM utilisateurs WHERE email = ?", (email,))
    user_data = cursor.fetchone()

    if user_data:
        user_id, hashed_password = user_data
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return User(user_id)

    return None


# Fonction pour récupérer les données de récapitulatif des absences
def get_absences_recap_data():
    conn = sqlite3.connect("C:/Users/Rab/Documents/DIT-s-projet-22-23/Projet/DIT_Projet.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nom_etudiant, nom_matiere, COUNT(*) AS total_absences
        FROM Presences
        WHERE statut_absence = 'absent'
        GROUP BY nom_etudiant, nom_matiere
    """)

    absences_recap_data = cursor.fetchall()
    conn.close()

    return absences_recap_data


# Fonction pour récupérer les données des étudiants
def get_students_data():
    conn = sqlite3.connect("C:/Users/Rab/Documents/DIT-s-projet-22-23/Projet/DIT_Projet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notes")
    students_data = cursor.fetchall()
    conn.close()
    return students_data


# Fonction pour récupérer les données de présence
def get_presences_data():
    conn = sqlite3.connect("C:/Users/Rab/Documents/DIT-s-projet-22-23/Projet/DIT_Projet.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nom_etudiant, nom_matiere, date_absence, statut_absence
        FROM Presences
    """)

    presences_data = cursor.fetchall()
    conn.close()

    return presences_data

# Insertion d'un nouvel utilisateur dans la base de données
def insert_new_user(email, password):
    # Connexion à la base de données
    conn = sqlite3.connect("C:/Users/Rab/Documents/DIT-s-projet-22-23/Projet/DIT_Projet.db")
    cursor = conn.cursor()

    # Vérifier si l'email existe déjà dans la base de données
    cursor.execute("SELECT COUNT(*) FROM utilisateurs WHERE email = ?", (email,))
    user_count = cursor.fetchone()[0]

    if user_count > 0:
        # L'email existe déjà, renvoyer False pour indiquer un échec d'inscription
        conn.close()
        return False

    # Hacher le mot de passe avant de l'insérer dans la base de données
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insérer le nouvel utilisateur dans la table utilisateurs
    cursor.execute("INSERT INTO utilisateurs (email, mot_de_passe) VALUES (?, ?)", (email, hashed_password))
    conn.commit()
    conn.close()

    return True  

# Route pour afficher la page de connexion
@app.route('/')
def display_login():
    return render_template('login.html')

# Route pour gérer la connexion
@app.route('/connexion', methods=['GET', 'POST'])
def handle_connexion():
    error_message = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = verify_credentials(email, password)
        if user:
            login_user(user)
            return redirect(url_for('display_accueil'))
        else:
            error_message = "Identifiants invalides. Veuillez réessayer."

    return render_template('login.html', error_message=error_message)

# Route pour afficher la page d'accueil (requiert une connexion)
@app.route('/acceuil')
@login_required
def display_accueil():
    return render_template('accueil.html')

# Route pour afficher les notes des étudiants (requiert une connexion)
@app.route('/notes')
@login_required
def display_students_data():
    students_data = get_students_data()
    return render_template('notes.html', students_data=students_data)

# Route pour afficher les données de récapitulatif des absences (requiert une connexion)
@app.route('/recap_absences.html')
@login_required
def display_recap_absences():
    absences_recap_data = get_absences_recap_data()
    return render_template('recap_absences.html', absences_recap_data=absences_recap_data)

# Route pour afficher l'historique des présences (requiert une connexion)
@app.route('/historique_presences.html')
@login_required
def display_historique_presences():
    presences_data = get_presences_data()
    return render_template('historique_presences.html', presences_data=presences_data)

# Route pour gérer l'inscription de nouvaux utilisateurs
@app.route('/inscription', methods=['GET', 'POST'])
def handle_inscription():
    error_message = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Vérifier si les mots de passe correspondent
        if password != confirm_password:
            error_message = "Les mots de passe ne correspondent pas. Veuillez réessayer."
        else:
            # Inscrire le nouvel utilisateur dans la base de données
            if insert_new_user(email, password):
                # Rediriger vers la page d'accueil après une inscription réussie
                error_message = "L'inscription de cet utilisateur c'est bien passée"
            else:
                error_message = "Cet email est déjà utilisé. Veuillez en choisir un autre."

    # Si la méthode est GET ou si l'inscription a échoué, afficher la page d'inscription avec le message d'erreur
    return render_template('inscription.html', error_message=error_message)

# Cette condition vérifie si le script Python est exécuté en tant que programme principal.
    # Si c'est le cas, la méthode app.run() sera appelée pour démarrer le serveur Flask.    
if __name__ == '__main__':
    app.run(debug=True)
