# Plateforme Web de Suivi des Étudiants du DIT

Projet de fin d'année universitaire 2022-2023 réalisé au Dakar Institute of Technology dans le cadre de la Licence (Big Data).

## Objectif

Cette plateforme vise à offrir aux responsables pédagogiques un outil numérique efficace pour le suivi académique des étudiants :
- Consultation des notes
- Suivi des présences et absences
- Génération de rapports et classements
- Visualisation des performances via graphiques interactifs

## Technologies utilisées

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js (visualisation des données)

### Backend
- Python
- Flask (framework web)

### Base de données
- MySQL

### Sécurité
- Authentification/autorisation sécurisée
- Chiffrement des données sensibles

## Fonctionnalités principales

- Connexion sécurisée
- Dashboard de suivi global (graphiques, courbes, statistiques)
- Affichage des notes avec recherche par étudiant ou matière
- Historique des présences et récapitulatif des absences
- Gestion des utilisateurs (ajout de nouveaux responsables pédagogiques)
- Déconnexion sécurisée

## Installation locale

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Royce-LAYINDE/DIT-s-projet-22-23.git
   cd DIT-s-projet-22-23

2. (Optionnel) Créer un environnement virtuel :

```bash
  python -m venv venv
  source venv/bin/activate  # ou venv\Scripts\activate sous Windows
  ```
3. Installer les dépendances :

```bash
  pip install -r requirements.txt
  ```
4. Lancer le serveur Flask :

```bash
  flask run
  ```
5. Accéder à l’application :

```bash
  http://localhost:5000
  ```
## Équipe projet
- LAYINDE Malick Royce
- Abdoulaye NDOUR
Encadré par M. Dominique NDOUR, Responsable pédagogique et marketing au DIT.

## Perspectives
- Des évolutions futures sont envisagées :
- Notifications automatiques en cas d’absences répétées
- Intégration avec d'autres systèmes du DIT
-Interface mobile adaptée

## Remerciements
Nous remercions l’équipe pédagogique du DIT pour son soutien, ainsi que nos encadreurs pour leurs précieux conseils.

## Licence
Projet académique réalisé dans le cadre de la formation à Dakar Institute of Technology. Toute utilisation hors cadre pédagogique nécessite une autorisation.
