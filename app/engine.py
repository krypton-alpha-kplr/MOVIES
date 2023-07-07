
#       ENGine.PY

#!pip install flask
#! pip install findspark
#!pip install pyspark


#1: Importation des bibliothèques nécessaires
from pyspark.sql.types import *
from pyspark.sql.functions import explode, col
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SQLContext

import app.py

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
        n=1         # nombres d'éléments de l'échantillon
        if movie_id==None : film = best_movies_df.sample(n) # film=best_movies_df[sample(1:nrow(best_movies_df),n), ]
        # Sinon, elle filtre le dataframe movies_df pour obtenir le film correspondant à movie_id.
        else:film=movies_df.filter(movies_df.movieId(movie_id))
        #film=movies_df[movies_id]
        # Méthode pour obtenir les évaluations d'un utilisateur
        film=movies_df.filter(movies_df.userId(user_id))
        #La méthode retourne un dataframe contenant les informations du film (colonne "movieId" et "title").
        return (
            moviesDF.filter(moviesDF.movieID(movie_id) , moviesDF.title \
                .groupBy(col("movieId"),col("title").orderBy("title", ascending=False) ) )
        )

    def get_ratings_for_user(self, user_id):
        # Méthode pour obtenir les évaluations d'un utilisateur
        #Elle prend en paramètre un user_id et filtre le dataframe ratings_df pour obtenir les évaluations correspondantes à l'utilisateur.
        rat=ratings_df.filter(ratings_df.userId(user_id) )
        # La méthode retourne un dataframe contenant les évaluations de l'utilisateur (colonnes "movieId", "userId" et "rating").
        return(rat)

    def add_ratings(self, user_id, ratings):
        # Méthode pour ajouter de nouvelles évaluations et re-entraîner le modèle. au modèle & re-entraîner le modèle.
        # Elle prend en paramètres un user_id et une liste de ratings contenant les nouvelles évaluations.
        # méthode crée 1 nvx dataframe new_ratings_df à partir de la liste de ratings & l'ajoute au dataframe existant ratings_df en utilisant l'opération union().
        new_ratings_df=ratings_df.union(ratings)
        #Données sont divisées en ensembles d'entraînement (training) et de test (test) en utilisant la méthode randomSplit().
        # with department table in order to check the inconsistent behaviour of randomsplit
        train, test = new_ratings_df.randomSplit([0.8, 0.2])
        X_new = train["train.movieId","train.title"]
        y_new = train["train.rating"]
        
        #Enfin, la méthode privée __train_model() est appelée pour re-entraîner le modèle(de manière incrémentale avec les nouvelles données)
        self.__train_model().partial_fit(X_new, y_new)
        # Enregistrer le modèle mis à jour dans un fichier
        #pickle.dump(self.model, open("model.pkl", "wb"))

    def predict_rating(self, user_id, movie_id):
        # Méthode pour prédire une évaluation pour un utilisateur & un film donnés.
        # creer un dataframe rating_df à partir des données (user_id, movie_id) & le transforme en utilisant le modèle pour obtenir les prédictions.
        # Prédire les étiquettes avec le modèle
        rating_df = self.__train_model.predict(user_id, movie_id)
        # Retourner Predictions: Si le dataframe de prédiction est vide, la méthode retourne -1, sinon elle retourne la valeur de prédiction.
        if (len(rating_df)>=0) : return (-1)
        else : return (rating_df)


    def recommend_for_user(self, user_id, nb_movies):
        # Méthode pour obtenir les meilleures recommandations pour un utilisateur donné.
        # Elle prend en paramètres un user_id et un nombre de films nb_movies à recommander.
        # Méthode crée un dataframe user_df contenant l'identifiant de l'utilisateur et utilise la méthode recommendForUserSubset() du modèle pour obtenir les recommandations pour cet utilisateur.
        user_df= user_id.union(recommendForUserSubset(user_id) )
        # Les recommandations sont ensuite jointes avec le dataframe movies_df pour obtenir les détails des films recommandés.
        # select*
        recommand_df=user_df \
                .join(movies_df,"movieId") \
                .select("title","userId", "movieId") \
                .orderBy("movieId") \
                .toPandas()
        # Le dataframe résultant est retourné avec les colonnes "title" et d'autres colonnes du dataframe movies_df.
        return recommand_df

    def __train_model(self):
        # Méthode privée pour entraîner le modèle avec l'algorithme ALS (Alternating Least Squares).
        #Elle utilise les paramètres maxIter et regParam définis dans l'initialisation de la classe pour créer une instance de l'algorithme ALS.
        als = ALS(maxIter=5,
          regParam=0.01,
          #, implicitPrefs=False,
          userCol="userId",
          itemCol="movieId",
          ratingCol="rating",
          #coldStartStrategy="drop"
          #, nonnegative=True
          )
        # Ensuite, le modèle est entraîné en utilisant le dataframe training.
        #with T():
        #    model = als.fit(trainingDF)
        model = als.fit(self.ratings_df)
        # La méthode privée __evaluate() est appelée pour évaluer les performances du modèle.
        self.__evaluate(model)
        # retourne le modèle entraîné
        return model


    def __evaluate(self):
        # Méthode privée pour évaluer le modèle en calculant l'erreur quadratique moyenne(RMSE,Root-mean-square error)
        # Elle utilise le modèle pour prédire les évaluations sur le dataframe test.
        
        # Ensuite, elle utilise l'évaluateur de régression pour calculer le RMSE en comparant les prédictions avec les vraies évaluations.
        from pyspark.ml.evaluation import RegressionEvaluator
        # Define evaluator as RMSE and print length of evaluator
        evaluator = RegressionEvaluator(
           metricName="rmse",
           labelCol="rating",
           predictionCol="prediction")
        #print ("Num models to be tested: ", len(param_grid))
        # La valeur de RMSE est stockée dans la variable rmse de la classe et affichée à l'écran.
        #rmse=rmse.union(evaluator)
        rmse = evaluator.evaluate(predictions)
        # Lower values of RMSE indicate better fit
        print("Root-mean-square error = " + str(rmse))



        # Méthode d'initialisation pour charger les ensembles de données & entraîner le modèle.
        # est appelée lors de la création d'une instance de la classe RecommendationEngine.
        # Paramètres le contexte Spark (sc), le chemin vers l'ensemble de données de films (movies_set_path) & le chemin vers l'ensemble de données d'évaluations (ratings_set_path).
    def __init__(self, sc, movies_set_path, ratings_set_path):
        # La méthode initialise le contexte SQL à partir du contexte Spark,
        #  charge les données des ensembles de films & d'évaluations à partir des fichiers CSV spécifiés,
        #  définit le schéma des données,
        #  effectue diverses opérations de traitement des données
        # & entraîne le modèle en utilisant la méthode privée __train_model().
        
        # initialise le contexte SQL à partir du contexte Spark
        self.spark = SparkSession(sc)
        # charge les données des ensembles de films & d'évaluations à partir des fichiers CSV spécifiés
        self.movies_df = self.spark.read.csv(movies_set_path, header=True)
        self.ratings_df = self.spark.read.csv(ratings_set_path, header=True)
        # définit le schéma des données
        self.movies_df = self.movies_df.withColumn("movieId", self.movies_df["movieId"].cast("int"))
        self.ratings_df = self.ratings_df.withColumn("userId", self.ratings_df["userId"].cast("int"))
        self.ratings_df = self.ratings_df.withColumn("movieId", self.ratings_df["movieId"].cast("int"))
        self.ratings_df = self.ratings_df.withColumn("rating", self.ratings_df["rating"].cast("float"))
        # effectue diverses opérations de traitement des données
        self.movies_df = self.movies_df.dropna()
        self.ratings_df = self.ratings_df.dropna()
        # entraîne le modèle en utilisant la méthode privée __train_model()
        self.model = self.__train_model()


# Création d'une instance de la classe RecommendationEngine
engine = RecommendationEngine(sc, "chemin_vers_ensemble_films", "chemin_vers_ensemble_evaluations")


#Pour utiliser la classe RecommendationEngine, créer une instance en passant le contexte Spark (sc)
# ainsi que les chemins vers les ensembles de données de films (movies_set_path) & d'évaluations (ratings_set_path).

# Exemple d'utilisation des méthodes de la classe RecommendationEngine
user_id = engine.create_user(None)
if engine.is_user_known(user_id):
    movie = engine.get_movie(None)
    ratings = engine.get_ratings_for_user(user_id)
    engine.add_ratings(user_id, ratings)
    prediction = engine.predict_rating(user_id, movie.movieId)
    recommendations = engine.recommend_for_user(user_id, 10)




