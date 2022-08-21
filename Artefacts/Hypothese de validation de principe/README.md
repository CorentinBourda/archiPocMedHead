# Hypothèse de validation des principes

Notre PoC a pour but de démontrer la faisabilié du projet de MedHead sur les aspects cruciaux liés aux enjeux du secteur médical. Traitant des urgence parfos vitales, le fonctionement de ntre futur API se doit d'être à tous les niveaux irréprochable et nous devons ainsi vérifier que cela est réalisable avec les technoogies à notre disposition.
Nous avons écrit des scripts permettant de faire des rapports d'excution permettant de démontrer le fonctionement des différents aspects crucieaux que l'API devra respecter pour fonctionner. Les scripts python nous ayant servis à écrire les rapports de tests afin de constituer notre PoC sont disponibles [ici](/artefacts/api_poc.py)
Afin de vérifier quel serveur répond à nos requêtes, le endpoint renvoie le nom du host qui a répondu. Les noms des hôtes sont: machine-poc-medhead-production-1 pour le premier serveur et machine-poc-medhead-production-2 pour le second.
- Tests de l'application:
  Afin de nous assurer qu'aucune régression ne pourra venir perturber le fonctionement des prises en charge, ce qui aurrait un impact dramatique, nous devons nous assurer qu'il est possible de mettre en place une API avec un niveau de test convenable à même de détecter tout type de régression. Le code coverage devra être supérieur à 80%
  - Méthodologie:
    Nous écrirons des tests untaires, d'intégration et end-to-end dans l'application spring boot puis nous calculerons le code coverage grâce à l'outil SonarQube
  - Résultats:
    Nous avons mis en place des tests relatifs à tous les composants de l'application afin de nous assurer de la qualité du code produit. Afin de ne pas permettre la mise en production d'erreurs dans le code, nous avons intégré les tests dans les pipelines de déploiement du code de gitHub actions. Ces pipelines détectent automatiquement toutes les régressions dans le code et empêchent la mise en production d'erreurs.

- Haute disponibilité:
  Les serveurs de notre API se devront d'être en permanence disponibles afin de toujours permettre une prise en charge. Nous devrons donc vérifier qu'en aucun ceux ci peuvent mettre en péril la prise en charge des patients en perturbant le fonctionement de l'application
  - Méthodologie:
    Nous provoquerons voulontairement la fermeture de serveurs qui assurent le fonctionement de l'application et nous vérifierons que l'application continue à tourner comme précédement avec le même nombre de nodes. Le script dressant les rapports de tests exécute d'abord 20 appels sur l'API dont nous devons vérifier qu'ils ont distribués sur les 2 serveurs. Une fois les 20 appels effectués nous mettons le premier serveur hors-service et nous étudions le comportement de l'API.
  - Résultats:
    Nous avons fait des tests de haute disponibilité dont le rapport est disponible dans le fichier [High Disponibility](/artefacts/high_disponibility.txt).
    Sur le rapport de l'exécution nous pouvons voir que les 20 premières requètes s'effectuent en répartition sur les 2 serveurs. Une fois que nous mettons le premier serveur hors service, les 20 dernières requêtes sont effectuées uniquement sur le second serveur, **ce qui prouve que l'API peut continuer de fonctionner après l'interuption d'un service**
    Une fois le premier serveur mis hors service, le container spring boot pourra être remis sur pied de façon automatique grâce aux fonctionalités des objets Docker service

- Grande charge de requêtes:
  Les serveurs devront pouvoir être capables de résister à de grande charges de réquêtes, avec un nombre très important d'utilisateurs qui recherchent un hopital en même temps
  - Méthodologie:
    Nous ferons un script Python afin de faire 100 requêtes en un laps de temps très court et nous vérifierons que toutes les requêtes ont étées éxécutées.
  - Résultats:
    Le rapport d'exécution du script python est disponible dans le fichier [Numerous Requests](/artefacts/numerous_requests.txt).
    Le script python exécuté montre que 100 réquêtes ont été effectués, toutes ayant des codes de succès. Cela montre que les serveurs sont capables d'encaisser un fort trafic et répartir la charge entre les deux serveurs.

- Temps de réponse:
  Afin de ne pas ralentir les prises en charge es patient, nous veillerons à vérifier que les temps de réponse de l'application n'éxèdent jamais 1000ms, même avec des requêtes en masse comme nous en ferons pour valider l'hypothèse précédente, afin d'assurer une rapidité dans la recherche de l'hopital.
  - Méthodologie:
    Dans le même script python évoqué ci-dessus nous ferons en sorte de calculer le temps de réponse et nous vérifierons que celui-ci n'éxcède jamais 1000ms
  - Résultats:
    Le rapport d'exécution du script python est disponible dans le fichier [Response Time](/artefacts/response_time.txt).
    Le rapport des éxécution montre bien que sur un total de 10 requêtes, le temps de réponse moyen est de moins de une seconde (0.98s) ce qui confirme notre hypothèse.
    Le temps de réponse reste cependant assez conséquent et beaucoup de facteurs peuvent venir le diminiuer. Tout d'abord, nous utilisons des serveurs digital ocean tous situés en Angleterre et aux états unis. Cela impacte beaucoup le temps de réponse et l'utilisation de serveurs français uniquement pourrais le diminuer. De plus, l'appel à l'API de MapBox ralentit le procesus et l'utilisation de serveurs de GeoCoding à l'intérieur de notre cluster pourra considérablement réduire le temps de réponse. Ces améliration nécésittent d'invetir du temps de développement, il sera possible de les mettre en place lors du développement de l'application.

| Hypothèse                                                                                                                                                  | Méthodologie                                                                                                                                                  | Résutat                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tests de l'application|Nous écrirons des tests untaires, d'intégration et end-to-end dans l'application spring boot.|Les tests couvrent bien tous les composants mis en place pour l'application spring-boot|
| Haute disponibilité| Nous provoquerons voulontairement la fermeture de serveurs qui assurent le fonctionement de l'application et nous vérifierons que l'application continue à tourner comme précédement avec le même nombre de nodes. |L'API peut tourner après interuption d'un service. Celui-ci peut se remettre en place tout seul grâce aux fonctionalités des docker services.|
| Grande charge de requêtes |Nous ferons un script Python afin de faire 100 requêtes en un laps de temps très court et nous vérifierons que toutes les requêtes ont étées éxécutées.|Le rapport montre 100 requêtes effectuées en un court laps de temps toutes réparties entre les deux serveurs du cluster Swarm|
| Temps de réponse | Dans le même script python évoqué ci-dessus nous ferons en sorte de calculer le temps de réponse et nous vérifierons que est de moins de 1000ms|Le temps de réponse moyen est de 1000ms. Ce résultat reste perfectible mais de très nombreux facteurs détaillés plus haut permettent de l'améliorer|
