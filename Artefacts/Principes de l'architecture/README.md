Nos principes architecturaux s'appuient sur les règles déffinies par le TOGAF.

**Matrice des risques:**
Afin de permettre aux équipes de se préparer le mieux possible aux risques du projets et d'identifier les plus dangereux nous devons mettre en place une matrice des risques

| Risque                                                                                                                                                  | Gravité                                                                                                                                                  | Probabilité                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Des régressions s'immiscent dans l'application en production ||
| Haute disponibilité| Nous provoquerons voulontairement la fermeture de serveurs qui assurent le fonctionement de l'application et nous vérifierons que l'application continue à tourner comme précédement avec le même nombre de nodes. |  |
| Grande charge de requêtes |Nous ferons un script Python afin de faire 200 requêtes en un laps de temps très court et nous vérifierons que toutes les requêtes ont étées éxécutées.||
| Temps de réponse | Dans le même script python évoqué ci-dessus nous ferons en sorte de calculer le temps de réponse et nous vérifierons que celui-ci n'éxcède jamais 200ms||
