# Utiliser une image de base existante
# FROM ubuntu:latest
FROM spark:3.4.0
FROM python:3.8-slim-buster

# Installer les dépendances de l'application
RUN apt-get update && apt-get install -y python3 python3-pip

# Copier les fichiers de l'application dans le conteneur
COPY . /app
# COPY . .

# Définir le répertoire de travail
WORKDIR /app

COPY requirements.txt requirements.txt

# Installer les dépendances de l'application
RUN pip3 install -r requirements.txt

# Exposer le port utilisé par l'application
EXPOSE 8080

# Définir la commande d'entrée d'exécution par défaut dans Dockerfile :
CMD ["spark-submit", "server.py", "ml-latest/movies.csv", "ml-latest/ratings.csv"]
