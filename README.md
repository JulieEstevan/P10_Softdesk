# Softdesk API (English)

Softdesk is a REST API developed with Django REST Framework. It enables collaborative management of projects, issues, and comments, while complying with GDPR standards. Environment and dependency management is handled by Pipenv.

## Table of Contents
- [Softdesk API (English)](#softdesk-api-english)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Resources](#resources)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Authentication](#authentication)
- [Softdesk API (Français)](#softdesk-api-français)
  - [Sommaire](#sommaire)
  - [Fonctionnalités](#fonctionnalités)
  - [Ressources](#ressources)
  - [Installation](#installation-1)
  - [Utilisation](#utilisation)
  - [Authentification](#authentification)

## Features

- User management with GDPR consent and age verification (>15 years)
- JWT authentication
- Project creation and management (name, description, type)
- Assigning contributors to projects
- Issue creation and management (priority, tag, status, assignment)
- Adding comments to issues
- Access control based on contributors
- Pagination of resource lists
- Automatic timestamping of each resource
- Resource ownership management (edit/delete reserved for the author)

## Resources

- **User**: Users with consent and age management
- **Contributor**: Link between a user and a project
- **Project**: Projects (back-end, front-end, iOS, Android)
- **Issue**: Project tasks/issues (priority, tag, status, assignment)
- **Comment**: Comments on issues, identified by UUID

## Installation

1. Clone the repository:
        ```
        git clone <repo-url>
        cd P10_Softdesk
        ```
2. Install Pipenv and dependencies:
        ```pip install pipenv```
        ```pipenv install```
        ```pipenv shell ```
3. Apply migrations:
        ```bash
        python manage.py migrate
        ```
4. Start the server:
        ```
        python manage.py runserver
        ```

## Usage

The API is available locally at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The API exposes endpoints to manage users, projects, issues, and comments. Refer to the API documentation (Swagger or Redoc) for more details.
Swagger:
[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
Redoc:
[http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

## Authentication

Authentication is handled via JWT. After logging in, include the token in the `Authorization` header of each request:
```
Authorization: Bearer <your_jwt_token>
```

---

© Softdesk

# Softdesk API (Français)

Softdesk est une API REST développée avec Django REST Framework. Elle permet la gestion collaborative de projets, de tâches (issues) et de commentaires, tout en respectant les normes RGPD. La gestion des environnements et des dépendances est assurée par Pipenv.

## Sommaire
- [Softdesk API (English)](#softdesk-api-english)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Resources](#resources)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Authentication](#authentication)
- [Softdesk API (Français)](#softdesk-api-français)
  - [Sommaire](#sommaire)
  - [Fonctionnalités](#fonctionnalités)
  - [Ressources](#ressources)
  - [Installation](#installation-1)
  - [Utilisation](#utilisation)
  - [Authentification](#authentification)

## Fonctionnalités

- Gestion des utilisateurs avec consentement RGPD et vérification de l'âge (>15 ans)
- Authentification par JWT
- Création et gestion de projets (nom, description, type)
- Attribution de contributeurs à des projets
- Création et gestion d'issues (priorité, balise, statut, assignation)
- Ajout de commentaires sur les issues
- Contrôle d'accès basé sur les contributeurs
- Pagination des listes de ressources
- Horodatage automatique de chaque ressource
- Gestion des droits d'auteur sur les ressources (modification/suppression réservée à l'auteur)

## Ressources

- **User** : Utilisateurs avec gestion de consentement et âge
- **Contributor** : Lien entre un utilisateur et un projet
- **Project** : Projets (back-end, front-end, iOS, Android)
- **Issue** : Tâches/problèmes d'un projet (priorité, balise, statut, assignation)
- **Comment** : Commentaires sur les issues, identifiés par UUID

## Installation

1. Clonez le dépôt :
        ```bash
        git clone <url-du-repo>
        cd P10_Softdesk
        ```
2. Installez Pipenv et les dépendances :
        ```bash
        pip install pipenv
        pipenv install
        pipenv shell
        ```
3. Appliquez les migrations :
        ```bash
        python manage.py migrate
        ```
4. Lancez le serveur :
        ```bash
        python manage.py runserver
        ```

## Utilisation

L'API est accessible à l'adresse suivante en local :  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

L'API expose des endpoints pour gérer les utilisateurs, projets, issues et commentaires. Consultez la documentation de l'API (Swagger ou Redoc) pour plus de détails.
Swagger:
[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
Redoc:
[http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

## Authentification

L'authentification se fait via JWT. Après connexion, incluez le token dans l'en-tête `Authorization` de chaque requête :
```
Authorization: Bearer <votre_token_jwt>
```

---

© Softdesk