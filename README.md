# Project-3-football
Objectif : Choisir, mettre en place, et peupler une base de données à partir d’un jeu de données (transfert de footballà), et implémenter une API permettant de requêter cette base de données.

# Choix de la base de données:
Nous avons choisi mongodb comme base car elle n'exige pas la création d'un schéma relationnel, ni de table. Cela n'est pas nécessaire pour un dataset aussi petit que celui que nous avons. Les performances de requêtage ne seront donc pas impactées.

# Première partie : Création de la base de données

	dossier insert_data_in db : pour la création de la base de données mongo et l'insertion des données
    - Dockerfile : construit l'image avec les librairies permettant de lancer footdbsetup.py
		- top250-00-19.csv données relatifs aux transferts de football que l'on insert dans la base de données mongo
		- footdbsetup.py : creer la base de données et insert le contenant du fichier csv dans celle-ci

# Deuxième partie : Création de l'API
    - Dockerfile : construit l'image avec les librairies permettant de lancer server.py
    - server.py : crée 4 endpoint permettant d'intéragir avec la base de données créeé dans la partie une
      - /status : retourne un message au client confirmant le bon fonctionnement de l'API
      - /mongodbstatus : retourne un message au client concernant l'état de la connexion à la base de données ok ou ko
      - /get_player_byname : retourne tous les transferts du joueur dont le "name" est fourni en paramètre
      - /add_player : ajoute un nouveau transfert dans la base de données à partir des informations sur le tranfert fourni en paramètre

# Troisième partie : Appel d'un client à l'API
		
	dossier test_football_api : pour l'appel à l'API
		- Dockerfile : construit l'image avec les librairies permettant de lancer test_api.py qui à pour objectif de tester l'API crée dans la deuxième partie
		test_api.py : contient la définition et l'appel des fonctions permettant de faire appel à l'API avec 4 fonctions définies
				- test de fonctionnement de l'api
				- test de connexion à la base de données
				- Recherche d'un joueur dans la base de données
        - Ajout d'un joueur dans la base de données

Executer la commande suivante pour lancer le projet :

./setup.sh
