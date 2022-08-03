# Hypothèse de validation des principes

Notre PoC a pour but de démontrer la faisabilié du projet de MedHead sur les aspects cruciaux liés aux enjeux du secteur médical. Traitant des urgence parfos vitales, le fonctionement de ntre futur API se doit d'être à tous les niveaux irréprochable et nous devons ainsi vérifier que cela est réalisable avec les technoogies à notre disposition.

- Tests de l'application:
  Afin de nous assurer qu'aucune régression ne pourra venir perturber le fonctionement des prises en charge, ce qui aurrait un impact dramatique, nous devons nous assurer qu'il est possible de mettre en place une API avec un niveau de test convenable à même de détecter tout type de régression. Le code coverage devra être supérieur à 80%
  - Méthodologie:
    Nous écrirons des tests untaires, d'intégration et end-to-end dans l'application spring boot puis nous calculerons le code coverage grâce à l'outil SonarQube
  - Résultats:
    N

- Haute disponibilité:
  Les serveurs de notre API se devront d'être en permanence disponibles afin de toujours permettre une prise en charge. Nous devrons donc vérifier qu'en aucun ceux ci peuvent mettre en péril la prise en charge des patients en perturbant le fonctionement de l'application
  - Méthodologie:
    Nous provoquerons voulontairement la fermeture de serveurs qui assurent le fonctionement de l'application et nous vérifierons que l'application continue à tourner comme précédement avec le même nombre de nodes.
  - Résultats:
    N

- Grande charge de requêtes:
  Les serveurs devront pouvoir être capables de résister à de grande charges de réquêtes, avec un nombre très important d'utilisateurs qui recherchent un hopital en même temps
  - Méthodologie:
    Nous ferons un script Python afin de faire 200 requêtes en un laps de temps très court et nous vérifierons que toutes les requêtes ont étées éxécutées.
  - Résultats:
    N

- Temps de réponse:
  Afin de ne pas ralentir les prises en charge es patient, nous veillerons à vérifier que les temps de réponse de l'application n'éxèdent jamais 200ms, même avec des requêtes en masse comme nous en ferons pour valider l'hypothèse précédente, afin d'assurer une rapidité dans la recherche de l'hopital.
  - Méthodologie:
    Dans le même script python évoqué ci-dessus nous ferons en sorte de calculer le temps de réponse et nous vérifierons que celui-ci n'éxcède jamais 200ms
  - Résultats:
    N

| Hypothèse                                                                                                                                                  | Méthodologie                                                                                                                                                  | Résutat                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tests de l'application|Nous écrirons des tests untaires, d'intégration et end-to-end dans l'application spring boot puis nous calculerons le code coverage grâce à l'outil SonarQube ||
| Haute disponibilité| Nous provoquerons voulontairement la fermeture de serveurs qui assurent le fonctionement de l'application et nous vérifierons que l'application continue à tourner comme précédement avec le même nombre de nodes. |  |
| Grande charge de requêtes |Nous ferons un script Python afin de faire 200 requêtes en un laps de temps très court et nous vérifierons que toutes les requêtes ont étées éxécutées.||
| Temps de réponse | Dans le même script python évoqué ci-dessus nous ferons en sorte de calculer le temps de réponse et nous vérifierons que celui-ci n'éxcède jamais 200ms||
