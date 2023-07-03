# MOVIES
TP Films imdb MOVIES


1.	Collecte des Données :

1.1 Source


La source est MovieLens (lentille) :
https://grouplens.org/datasets/movielens/


« recommended for education and development”, MovieLens Latest Datasets
These datasets will change over time, and are not appropriate for reporting research results. We will keep the download links stable for automated downloads. We will not archive or make available previously released versions.

Small: 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. Last updated 9/2018.

README.html
https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html
ml-latest-small.zip (size: 1 MB)
https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

Description
4 Fichiers « .CSV »
links.csv		194ko	
movies.csv		483ko	9742
ratings.csv		2426
tags.csv		116

Taille 



Stocker Gitpod/Databrick
Préalable :
Nouveau Dépôt GitHub :MOVIES







Se Loguer à databricks
Connexion - Databricks Community Edition
https://community.cloud.databricks.com/login.html

Compte:
alphakryptonkplr@gmail.com

Menu => Créer Cluster : movies
 
Pas d’option : “Free 15Gb Memory…”



Créer un Notebook : Menu -> create -> Notebook
Le langage par défaut du notebook est python

Menu : Upload Data to DBFS




1.3 Analyse Exploratoire EDA : Les colonnes (insights)

Nombre d’enregistrements
4 Fichiers « .CSV »	Taille		Nbr Enreg.
links.csv		194ko		9742
movies.csv		483ko		9742
ratings.csv		2426		100836
tags.csv		116		3683


Nombre de catégories : 12 ?
Adventure|Animation|Children|Comedy|Fantasy
Romance; Drama; Musical; Action; Sci-Fi; Horror; Western





Requetes :
Jointure:

Select Comedy Movies Only
Display the TOP rated Comedy Movies

MOST Rated Comedy Movies - No matter the rating

BEST Rated Comedy Movies
ou :
Changer de genre (à votre discrétion)
Comedy est juste un exemple (modifié) 

Most Rated Comedy Movies, grouped by Movie & Rating

Top Rated Comedy Movies with most rating
#
J'ai fait un join et je travaille désormais sur une table ou un Dataframe "commun" Movies / Ratings
Bonus 1:
Créer un Dataframe à part Pour les GENRES et les ID de genre, et dé-normaliser

Bonus 2 :
En faire de même pour tous les genres listés (automatiser via du code pour boucler autour d'une liste de genre pré-populée, ou même un dataframe de genre distincts - préférable)




Type d’apprentissage: Machine Learning

#

Filtrage Collaboratif
Filtrage collaboratif est un algorithme de recommandation, c'est-à-dire un algorithme qui consiste à prédire les articles (quels qu'ils soient, des livres, des films, des articles de presse, etc.) que des utilisateurs apprécieront dans le futur
https://fr.wikipedia.org/wiki/Filtrage_collaboratif
