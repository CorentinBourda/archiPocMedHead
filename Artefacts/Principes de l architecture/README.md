Nos principes architecturaux s'appuient sur les règles déffinies par le TOGAF.

**Matrice des risques:**
Afin de permettre aux équipes de se préparer le mieux possible aux risques du projets et d'identifier les plus dangereux nous devons mettre en place une matrice des risques

| Risque                                                                                                                                                  | Gravité                                                                                                                                                  | Probabilité                                                                                                                                              | Impact|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Des régressions s'immiscent dans l'application en production |5|4| Des prises en charges ne pourront pas se faire via notre application|
| Le temps de réponse est supérieur à 200ms|3|2| Les prises en charge seront un petit peu plus lentes|
| MapBox ne répond pas |5|1|Les prises en charge ne peuvent pas se faire via l'application|
| L'équipe de parvient pas à finir dans les temps| 3| 2| Le projet verra sa date de fin décalée|
| Tous les serveurs sont à l'arrêt| 5| 1| L'application ne fonctionne plus|

**A. Principes d'architectire de l'entreprise:**
- L'agilité
  - Afin d'être flexible et de pouvoir s'adapter à tous types de changements dans le projet, nous veillerons à appliquer les principes de la méthodoogie agile en veillant  laisser s'exprimmer les développeur pour qu'ils puissent approter un maximum au projet.
- Le risque 0
  - Cette application touchant à la prise en charge de patients dans des situtations souvent graves, il est très important que notre application n'ai aucune chance de ne pas fonctionner.
- La confidentialité
  - Travaillant dans le secteur médical, il et très important que nos données soint hautement protégées afin de ne pas révéler des informations sensibles sur nos patients.

**B. IT (Tests, DevOps, Sécurité, disponibilité): nos principes d'architecture:**
- Tests:
  - Le code coverage maximum: Afin de nous assurer de la qualité u code avant chaque livraison, nous pensons qu'il est très important de mettre en place une application avec un haut taux de code coverage (< 80%) ce qui permet d'éviter un maximum les régressions
  - Les différents niveaux de test: Afin de détecter un maximum de régressions, il sera primordial de faire différents types de tests selon le principe de la pyramide des tests comme cela est expliqué dans le [document de stratégie de test](∼/Artefacts/Document%20de%20strategie%20de%20test/README.md)
- DevOps:
  - Automatisation des processus: Afin de faire économiser du temps à nos équipes de développement, nous mettrons en place de pipelines à même de construire de nouvelles images Docker à chaque nouvelle fonctionalité livrée.
  - Intégration des tests dans la CI/CD: Nous intégrerons les tests dans la CI/CD afin de ne permettre à aucune régression de passer en production
- Sécurité
  - Afin de maximiser la sécurité, les comunication se feront uniquement via les network que nous pourrons mettre en place via Docker afin de minimiser les risques de vols de données. Le protcole HTTP est utilisé dans le cadre du développement de l'application cependant il sera primordial de mettre en place le protcole HTTPS pour l'application cible afin de garantir la sécurité des données.
- Disponibilité:
  - Mise en place de 2 serveurs: Afin de permettre la haute disponibilité de l'application nus mettrons en place 2 serveurs au sein d'un cluster Docker Swarm qui permettra de maintenir le fonctionement de l'application dans le cas où un des deux serveurs tombe en panne.

