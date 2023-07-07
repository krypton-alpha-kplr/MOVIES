
# APP.PY

!pip install flask
!pip install findspark
! pip install pyspark


# Flask et Blueprint pour créer l'application web.
from flask import Flask
from flask import Blueprint

# render_template pour charger les modèles de templates.
from flask import render_template

# json pour manipuler les données au format JSON.
import json
# findspark pour trouver et initialiser Spark.
import findspark

#SparkContext et SparkSession pour travailler avec Spark.
import pyspark
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext('local')
spark = SparkSession(sc) #Acceder aux donnees parralélisées

'''
#Create SparkSession
spark = SparkSession.builder
                    .master("local[1]")
                    .appName("SparkByExamples.com")
                    .getOrCreate()
sc=spark.sparkContext
'''

# importer RecommendationEngine (supposons qu'il s'agit d'un fichier engine.py) pour gérer les recommandations.
import engine.py

# Créez un Blueprint Flask :
# app = Flask(__name__)
main = Blueprint('main', __name__)

# Initialisez Spark :
findspark.init()

# Définissez la route principale ("/") :
@main.route("/", methods=["GET", "POST", "PUT"])
def home():
    return render_template("index.html")

# Définissez la route pour récupérer les détails d'un film :
@main.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    # Code pour récupérer les détails du film avec l'id spécifié
    df_m=movies_df(movie_id)
    # et renvoyer les données au format JSON
    return df_m.to_json(orient="records")

#6. Définissez la route pour ajouter de nouvelles évaluations pour les films : 
@main.route("/newratings/<int:user_id>", methods=["POST"])
def new_ratings(user_id):
    # Code pour vérifier si l'utilisateur existe déjà
    if (is_user_known(self, user_id) ==False ):
        # Si l'utilisateur n'existe pas, créez-le
        user_id=new(user_id)
    # Récupérez les évaluations depuis la requête et ajoutez-les au moteur de recommandation
    get_ratings_for_user(self, user_id)
    # Renvoyez l'identifiant de l'utilisateur si c'est un nouvel utilisateur, sinon renvoyez une chaîne vide
    if user_id>len(max_user_identifier) : return user_id
    else : return("")

#7. Définissez la route pour ajouter des évaluations à partir d'un fichier : 
@main.route("/<int:user_id>/ratings", methods=["POST"])
def add_ratings(user_id):
    # Code pour récupérer le fichier téléchargé depuis la requête
    df_rat=add_ratings(user_id)
    # Lisez les données du fichier et ajoutez-les au moteur de recommandation
    recommand_df=recommend_for_user(user_id, nb_movies) \
                .join(df_rat,"movieId") \
                .select("title","userId", "movieId") \
                .orderBy("movieId") \
                .toPandas()
    # Renvoyez un message indiquant que le modèle de prédiction a été recalculé
    return("modèle de prédiction a été recalculé OK")


# 8. Définissez la route pour obtenir la note prédite d'un utilisateur pour un film : 

@main.route("/<int:user_id>/ratings/<int:movie_id>", methods=["GET"])
def movie_ratings(user_id, movie_id):
    # Code pour prédire la note de l'utilisateur pour le film spécifié
    prdct_rat=predict_rating(user_id, movie_id)
    # Renvoyez la note prédite au format texte
    return prdct_rat.str

#9. Définissez la route pour obtenir les meilleures évaluations recommandées pour un utilisateur : 
@main.route("/<int:user_id>/ratings/<int:movie_id>", methods=["GET"])
def movie_ratings(user_id, movie_id):
    # Code pour prédire la note de l'utilisateur pour le film spécifié
    prdct_rat=predict_rating(user_id, movie_id)
    # Renvoyez la note prédite au format texte
    return prdct_rat.str

#10. Définissez la route pour obtenir les évaluations d'un utilisateur : 
@main.route("/ratings/<int:user_id>", methods=["GET"])
def get_ratings_for_user(user_id):
    # Code pour récupérer les évaluations de l'utilisateur spécifié
    prdct_rat=predict_rating(user_id)
    # Renvoyez les évaluations au format JSON
    return prdct_rat.to_json
    
#11. Creer fonction `create_app(spark_context, movies_set_path, ratings_set_path)` pour créer l'application Flask :
def create_app(spark_context, movies_set_path, ratings_set_path):
    # Code pour initialiser le moteur de recommandation avec le contexte Spark et les jeux de données
    init_engine(spark_context, movies_set_path, ratings_set_path)
    # Créez une instance de l'application Flask
    # Enregistrez le Blueprint "main" dans l'application
    # Configurez les options de l'application Flask
    # Renvoyez l'application Flask créée

    # Créez une instance de l'application Flask
    app = flask.Flask(__name__)

    # Enregistrez le Blueprint "main" dans l'application
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configurez les options de l'application Flask
    app.config.from_object('config')
    # Renvoyez l'application Flask créée
    return app


@app.route('/')
def index():
    return "This is an example app"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None): return render_template('hello.html', name=name)
