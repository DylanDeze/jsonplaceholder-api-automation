# API Automation Testing – Python

## 📌 Présentation
Ce projet a pour objectif de démontrer la mise en place d’un framework de tests automatisés pour une API REST en Python, en appliquant les bonnes pratiques de QA Automation.

Les tests couvrent les principales opérations CRUD (GET, POST, PUT, DELETE) et sont conçus pour être lisibles, maintenables et exécutables aussi bien en local qu’en environnement CI.

L’API testée est JSONPlaceholder, une API publique de démonstration.

---

## 🛠️ Technologies utilisées
- Python 3
- Pytest
- Requests
- pytest-html
- REST API
- Git / GitHub

---

## 🌐 API testée
JSONPlaceholder  
https://jsonplaceholder.typicode.com

---
**```text**
## 📁 Structure du projet

.
├── data/
│   └── post_payloads.py
│
├── utils/
│   └── api_client.py
│
├── tests/
│   ├── conftest.py
│   ├── test_get_posts.py
│   ├── test_create_post.py
│   ├── test_update_post.py
│   └── test_delete_post.py
│
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md

---

## 🧪 Scénarios de tests couverts

### ✅ TEST 1 — GET /posts
- Récupération de la liste des posts
- Vérification du status code 200
- Vérification que la réponse est une liste non vide
- Vérification de la présence des champs : userId, id, title, body

---

### ✅ TEST 2 — GET /posts/{id}
- Récupération d’un post existant
- Vérification du status code 200
- Vérification que l’ID retourné correspond à l’ID demandé
- Test d’un ID inexistant (status code 404)

---

### ✅ TEST 3 — POST /posts
- Création d’un post avec un payload valide
- Vérification du status code 201
- Vérification de la présence des champs retournés
- Test de la création avec un payload invalide

> Note : JSONPlaceholder est une API de démonstration et ne valide pas les payloads envoyés.  
> Les payloads incomplets retournent également un status code 201.  
> Les tests reflètent donc le comportement réel de l’API.

---

### ✅ TEST 4 — PUT /posts/{id}
- Modification d’un post existant
- Vérification du status code 200
- Vérification que les champs modifiés (title, body) ont bien été mis à jour
- Vérification que l’ID du post reste inchangé

---

### ✅ TEST 5 — DELETE /posts/{id}
- Suppression d’un post existant
- Vérification que le status code retourné est 200 ou 204

---

## ▶️ Installation et exécution

### 1️⃣ Cloner le projet

git clone https://github.com/<ton-username>/<nom-du-repo>.git
cd <nom-du-repo>


---

### 2️⃣ Créer et activer un environnement virtuel

python -m venv venv
source venv/bin/activate 
Windows : venv\Scripts\activate


---

### 3️⃣ Installer les dépendances

pip install -r requirements.txt


---

### 4️⃣ Lancer les tests

pytest

---

## 📊 Génération d’un rapport HTML

pytest --html=reports/report.html --self-contained-html


Le rapport est généré dans le dossier `reports/`.

---

## 🧠 Bonnes pratiques appliquées
- Tests indépendants
- Utilisation de fixtures Pytest
- Séparation de la logique API et des tests
- Externalisation des données de test
- Assertions explicites
- Structure maintenable et évolutive

---

## ⚠️ Limitations connues
- JSONPlaceholder ne persiste pas réellement les données
- Les validations serveur ne sont pas appliquées sur les payloads

Ces limitations sont documentées et prises en compte dans les tests.

---

## 🎯 Objectif du projet
Projet réalisé dans un objectif de montée en compétences et de démonstration professionnelle en QA Automation Python.

---

👤 Auteur : NGUESSAN Dylan - Projet personnel – QA Automation Python

