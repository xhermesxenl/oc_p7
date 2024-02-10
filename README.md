# Projet 7 : API de Scoring de Crédit

## Description

Ce projet concerne le développement et le déploiement d'une API de scoring de crédit pour "Prêt à dépenser", une entreprise financière spécialisée dans l'octroi de crédits à la consommation pour les personnes ayant peu ou pas d'historique de crédit.
L'objectif principal de l'API est de calculer automatiquement la probabilité de remboursement d'un crédit par un client et de classer la demande comme accordée ou refusée en fonction d'un seuil optimisé du point de vue métier.

## Architecture du Projet

L'API repose sur un modèle de scoring développé à partir de données comportementales et financières variées. 
Le projet suit une approche MLOps pour l'entraînement, le suivi, et le déploiement du modèle, en utilisant des outils tels que MLFlow pour le tracking des expérimentations, un registre centralisé des modèles, et GitHub Actions pour l'intégration et le déploiement continu.

### Découpage des Dossiers

- `/`: Code source pour l'entraînement du modèle, le déploiement de l'API, les tests unitaires, liste des packages.
- `Data/`: Contient les jeux de données utilisés pour l'entraînement et le test du modèle.
- `DataDrift/`: Contient le rapport data drift avec evidently.
- `MLFlow/`: Inclut le modèle entraîné, gérés par MLFlow.
- `Notebooks/`: Notebooks Jupyter pour l'analyse exploratoire, la préparation des données, le feature engineering et la modélisation.
- `Streamlit/`: Code source pour le tableau de bord Streamlit.

## Installation

Pour configurer et exécuter l'API localement, suivez ces étapes :

1. Clonez le dépôt GitHub.
2. Installez les dépendances en exécutant `pip install -r requirements.txt` dans le terminal.
3. Lancez l'API avec `python api.py`.

## Utilisation

L'API peut être testée localement via une requête HTTP POST avec un payload JSON contenant les données du client. Les instructions détaillées pour tester l'API sont disponibles dans `src/README.md`.

## Déploiement

Les instructions pour le déploiement de l'API sur une plateforme cloud (Heroku) sont fournies dans le fichier `DEPLOYMENT.md`.

## Outils et Packages Utilisés

Un fichier `requirements.txt` est inclus, listant toutes les bibliothèques Python nécessaires pour exécuter l'API.

## Licence
[MIT](https://choosealicense.com/licenses/mit/)

## Contributions

Les contributions sont les bienvenues.
