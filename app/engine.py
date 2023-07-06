#1: Importation des bibliothèques nécessaires
from pyspark.sql.types import *
from pyspark.sql.functions import explode, col
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SQLContext


class RecommendationEngine:

#méthode de creation nouvel utilisateur. prend en paramètre un user_id facultatif pour spécifier l'identifiant de l'utilisateur
    def create_user(self, user_id):
        #Si user_id est None, un nouvel identifiant est généré automatiquement.
        if user_id==None : new(user_id)
        #Si user_id est supérieur à max_user_identifier, max_user_identifier est mis à jour avec la valeur de user_id.
        if user_id>max_user_identifier : max_user_identifier=user_id
        # La méthode retourne l'identifiant de l'utilisateur créé ou mis à jour.
        return user_id

# méthode permet de vérifier si un utilisateur est connu.méthode permet de vérifier si un utilisateur est connu.
    def is_user_known(self, user_id) :
        # retourne True si l'utilisateur est connu (c'est-à-dire si user_id est différent de None & inférieur ou égal à max_user_identifier),
        if (user_id!=None ) & user_id<=max_user_identifier:
            return True
        # sinon elle retourne False.
        else : return False

def get_movie(self, movie_id):
        # Méthode pour obtenir un film
        #Si movie_id est None, la méthode retourne un échantillon aléatoire d'un film à partir du dataframe best_movies_df.
        if movie_id==None 
        # Sinon, elle filtre le dataframe movies_df pour obtenir le film correspondant à movie_id.

        #La méthode retourne un dataframe contenant les informations du film (colonne "movieId" et "title").
        return 



    def get_ratings_for_user(self, user_id):
        # Méthode pour obtenir les évaluations d'un utilisateur
        ...

    def add_ratings(self, user_id, ratings):
        # Méthode pour ajouter de nouvelles évaluations et re-entraîner le modèle
        ...

    def predict_rating(self, user_id, movie_id):
        # Méthode pour prédire une évaluation pour un utilisateur et un film donnés
        ...

    def recommend_for_user(self, user_id, nb_movies):
        # Méthode pour obtenir les meilleures recommandations pour un utilisateur donné
        ...

    def __train_model(self):
        # Méthode privée pour entraîner le modèle avec ALS
        ...

    def __evaluate(self):
        # Méthode privée pour évaluer le modèle en calculant l'erreur quadratique moyenne
        ...

    def __init__(self, sc, movies_set_path, ratings_set_path):
        # Méthode d'initialisation pour charger les ensembles de données et entraîner le modèle



















