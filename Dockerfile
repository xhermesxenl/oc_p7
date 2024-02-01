# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY requirements.txt ./
COPY api.py ./
COPY model.pkl ./
COPY test_api.csv ./
COPY train_api.csv ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=api.py

# Exposer le port sur lequel Flask va s'exécuter
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]
