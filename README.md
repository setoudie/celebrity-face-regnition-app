```text
Name : Seny Toutou DIEDHIOU
    --> Data Engieneer

```
# Application de Reconnaissance Faciale des Célébrités

Ce projet est une application de **reconnaissance faciale des célébrités** développée avec **Django** pour le backend, **React.js** pour le frontend, et **Firebase** pour le déploiement et le stockage. L'objectif du projet est de mieux comprendre le **machine learning** et de créer une application web moderne.

## Table des Matières

- [Aperçu du Projet](#aperçu-du-projet)
- [Technologies Utilisées](#technologies-utilisées)
- [Architecture du Projet](#architecture-du-projet)
- [Instructions d'Installation](#instructions-dinstallation)
- [Fonctionnalités](#fonctionnalités)
- [Améliorations Futures](#améliorations-futures)
- [Licence](#licence)

## Aperçu du Projet

Cette application permet aux utilisateurs de télécharger une image d'une célébrité, et le modèle de machine learning prédit quelle célébrité est sur l'image. Le projet combine des technologies web modernes avec le machine learning pour offrir une expérience interactive et conviviale.

## Technologies Utilisées

- **Backend** : Django (Python)
- **Frontend** : React.js (JavaScript)
- **Machine Learning** : TensorFlow ou OpenCV pour la reconnaissance faciale
- **Stockage & Hébergement** : Firebase (Firebase Storage, Firestore, Firebase Hosting)
- **Déploiement** : Firebase pour l'hébergement, Heroku pour les besoins backend éventuels
- **Base de données** : Firestore pour les métadonnées et les informations utilisateur

## Architecture du Projet

Le projet est structuré comme suit :

```
celebrity-face-regnition-app/
│
├── backend/                    # Code backend Django
│   ├── face_recognitions/      # Dossier du projet Django
│   ├── api/                    # Application Django pour gérer l'API
│   └── models/                 # Modèles de machine learning (TensorFlow, OpenCV)
│
├── frontend/                   # Code frontend React.js
│   ├── public/                 # Fichiers statiques pour React
│   ├── src/
│   │   ├── components/         # Composants React (UI)
│   │   ├── services/           # Services API et utilitaires
│   │   └── App.js              # Composant principal React
│
├── firebase/                   # Configuration Firebase pour le déploiement et le stockage
│   ├── firebase.json           # Configuration de l'hébergement Firebase
│   └── .firebaserc             # Paramètres du projet Firebase
│
├── ml_models/                  # Modèles de machine learning pré-entraînés ou personnalisés
│   ├── model.py                # Logique de chargement et d'inférence du modèle ML
│   └── trained_models/         # Modèles sauvegardés TensorFlow ou OpenCV
│
└── README.md                   # Fichier README du projet
```

### Backend (Django)

Le backend fournira l'API pour gérer les requêtes des utilisateurs, effectuer la reconnaissance faciale, et renvoyer les résultats au frontend. Les modèles de machine learning seront chargés dans le backend pour traiter les images et faire les prédictions.

### Frontend (React.js)

Le frontend est responsable de la présentation de l'interface utilisateur où les utilisateurs peuvent télécharger des images et voir les résultats. React.js communiquera avec le backend via des appels API pour effectuer les tâches de reconnaissance.

### Stockage et Déploiement (Firebase)

Firebase Storage est utilisé pour stocker les images téléchargées par les utilisateurs, et Firebase Hosting est utilisé pour servir le frontend. Firestore stocke les métadonnées et les données liées aux utilisateurs.

## Instructions d'Installation

### Backend (Django)
1. Clone le dépôt :
   ```bash
   git clone https://github.com/tonnomutilisateur/celebrity-face-regnition-app.git
   cd celebrity-face-regnition-app/backend
   ```
2. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configure l'environnement Django :
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend (React.js)
1. Va dans le répertoire `frontend` :
   ```bash
   cd ../frontend
   ```
2. Installe les dépendances :
   ```bash
   npm install
   ```
3. Démarre le serveur de développement :
   ```bash
   npm start
   ```

### Configuration Firebase
1. Configure Firebase en ajoutant tes informations d'identification Firebase dans le répertoire `firebase/`.
2. Déploie ton projet sur Firebase Hosting :
   ```bash
   firebase deploy
   ```

## Fonctionnalités

- **Authentification des Utilisateurs** : Authentification Firebase pour la connexion et l'inscription des utilisateurs.
- **Téléchargement d'Images** : Télécharge des images pour la reconnaissance des célébrités via le frontend React.
- **Reconnaissance Faciale** : Prédiction des célébrités à partir des images à l'aide de modèles de machine learning.
- **Affichage des Résultats** : Affichage des résultats de la reconnaissance sur le frontend.
- **Stockage Scalable** : Firebase Storage pour gérer les images téléchargées par les utilisateurs.
- **API** : API Django pour traiter les images et renvoyer les résultats.

## Améliorations Futures

- Améliorer la précision du modèle de machine learning en l'entraînant avec un dataset plus large.
- Ajouter une reconnaissance faciale en temps réel à partir d'un flux de caméra.
- Implémenter la prise en charge de plusieurs langues pour une accessibilité accrue.
- Améliorer l'interface utilisateur avec des animations et un meilleur design.
