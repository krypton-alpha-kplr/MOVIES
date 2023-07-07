# Dockerfile Utiliser une image de base existante
# FROM ubuntu:latest
FROM spark:3.4.0
#FROM python:3.8-slim-buster


# Installer les dépendances de l'application
# RUN apt-get update && apt-get install -y python3 python3-pip


# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt
COPY ./app/ml-latest /ml-latest

# Installer les dépendances de l'application
RUN pip3 install -r requirements.txt
#RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r workspace/MOVIES/requirements.txt
# RUN sed -i "s/localhost/$(curl http://checkip.amazonaws.com)/g" static/index.js


COPY . .

# Exposer le port utilisé par l'application
#EXPOSE 8080
EXPOSE 5432

# Définir la commande d'entrée d'exécution par défaut dans Dockerfile :
CMD ["spark-submit", "server.py", "ml-latest/movies.csv", "ml-latest/ratings.csv"]
