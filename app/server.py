
# 03_Creation_de_server.py.md

# Importez les bibliothèques nécessaires :
# time pour la gestion du temps.
import time
# sys pour accéder aux arguments de la ligne de commande.
import sys
# cherrypy pour créer le serveur web CherryPy.
import cherrypy
# os pour effectuer des opérations sur le système d'exploitation.
import os
# cheroot.wsgi pour le serveur WSGI CherryPy.
import cheroot.wsgi
# SparkContext et SparkConf pour travailler avec Spark.
from pyspark.context import SparkContext
import SparkConf

# create_app (supposons qu'il s'agit d'un fichier app.py) pour créer l'application Flask.
# import app.py
from app import create_app

from pyspark.sql import SparkSession

#Créez un objet SparkConf :
conf = SparkConf().setAppName("movie_recommendation-server")

# 3. Initialisez le contexte Spark & charger librairies:
sc = SparkContext(conf=conf, pyFiles=['engine.py', 'app.py'])

# SparkSession pour créer une session Spark.
spark = SparkSession(sc) #Acceder aux donnees parralélisées

# Obtenez les chemins des jeux de données des films et des évaluations à partir des arguments de la ligne de commande :
movies_set_path = sys.argv[1] if len(sys.argv) > 1 else ""
ratings_set_path = sys.argv[2] if len(sys.argv) > 2 else ""

# Créez l'application Flask :
app = create_app(sc, movies_set_path, ratings_set_path)

# Configurez et démarrez le serveur CherryPy :
cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                         'server.socket_port': 5432,
                         'engine.autoreload.on': False
                         })

if __name__ == '__main__':
    cherrypy.engine.start()

#Spark-movie-recommendation-md/03_Creation_de_server.py.md at main · ayoub
