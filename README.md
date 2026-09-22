
# 🌾 AgroMercado Backend API

Une API RESTful robuste construite avec **Django** et **Django REST Framework (DRF)** pour une plateforme e-commerce connectant les producteurs agricoles aux acheteurs.

---

## 🚀 Fonctionnalités Principales

- **Gestion des Utilisateurs & Authentification** : Authentification basée sur JWT (`rest_framework_simplejwt`) gérant l'inscription, la connexion et le rafraîchissement des jetons.
- **Catalogue de Produits** : Gestion complète des catégories et des produits (CRUD).
- **Gestion des Commandes** : Les acheteurs peuvent passer des commandes et consulter leur historique.
- **Documentation Interactive** : Interface Swagger UI et schéma OpenAPI générés dynamiquement via `drf-spectacular`.
- **Interface d'Administration** : Panneau Django Admin configuré pour la gestion des ressources.

---

## 🛠️ Stack Technique

- **Langage** : Python 3.10+
- **Framework** : Django 5.x, Django REST Framework
- **Authentification** : Simple JWT
- **Documentation** : OpenAPI 3.0 via `drf-spectacular` (Swagger UI)
- **Base de données** : SQLite (développement)

---

## ⚙️ Installation locale

\`\`\`bash
git clone https://github.com/banterialvibampoque-hub/agromercado_backend.git
cd agromercado_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\`\`\`

Accédez à l'application sur http://127.0.0.1:8000/ (documentation Swagger : `/api/docs/`, interface admin : `/admin/`).

## 📄 Licence

Ce projet est sous licence MIT.
EOF