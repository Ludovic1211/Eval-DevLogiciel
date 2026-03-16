# Application Dash - Avocado Dashboard

Application Dash de visualisation des ventes d'avocats aux États-Unis, développée dans le cadre du cours de développement logiciel du Master 2 MECEN de l'Université de Tours.

## Prérequis

- Python 3.10+
- [UV](https://github.com/astral-sh/uv) pour la gestion des dépendances

## Installation

### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd <nom-du-dossier>
```

### 2. Installer les dépendances

```bash
uv sync
```

## Lancement

```bash
uv run python app.py
```

L'application est disponible à l'adresse : **http://127.0.0.1:8050**

## Structure du projet

```
projet/
├── app.py                  # Fichier principal - lance l'application
├── pages/
│   ├── table.py            # Layout page 1 - Tableau de données
│   ├── table_cb.py         # Callbacks page 1
│   ├── compare.py          # Layout page 2 - Comparaison de régions
│   ├── compare_cb.py       # Callbacks page 2
│   └── markdown.py         # Layout page 3 - Aide en ligne
├── assets/
│   └── dash.jpg            # Image de fond page 3
├── datas/
│   └── avocado.csv         # Jeu de données
└── README.md
```

## Pages

### Page 1 — Affichage des données
Tableau interactif filtrable par région et par type d'avocat (conventionnel, biologique ou les deux).

### Page 2 — Comparaison entre régions
Deux graphiques côte à côte affichant l'évolution du prix moyen des avocats pour deux régions sélectionnables. Les deux graphiques partagent la même échelle pour faciliter la comparaison.

### Page 3 — Aide en ligne
Documentation de l'application présentée sous forme d'accordion avec trois sections : présentation de la page, explication du layout et explication des callbacks.

## Dépendances

| Package | Rôle |
|---|---|
| dash | Framework principal |
| dash-bootstrap-components | Composants Bootstrap pour Dash |
| pandas | Manipulation des données |
| plotly | Visualisation des graphiques |