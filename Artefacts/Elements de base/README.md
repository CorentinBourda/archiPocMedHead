# Éléments de bases

Tout au long de la mise de la mise en place de notre PoC nous avons eu l'ocasion de développer des élements qui pourront servir à l'équipe en charge de développer l'API de prise en charg des patients de MedHead
Ces éléments peuvent avoir une valeur pour le développement de la futur application et il nous parait important de les mentioner

1: API Spring Boot:
Nous avons pu développer lors de notre PoC ue API Spring Boot qui comporte un seul endpoint de création d'une réservation de lit ainsi que le code nécéssaire au fonctionement de celui ci dans les différentes couches de l'application. Nous avons aussi intégré les tests relatifs au fonctionement du endpoint. Cette API bien que rudimentaire pourrait aider les développeurs dans les premières étapes de la mise en place de l'application.

2: Pipelines GitLab:
Lors du dévelppement de notre PoC nous avons pu mettre en place des pipelines qui nous permettent de créer autmatiquement une image Docker nouvelle à chaque fois que du nuveau code arrive sur la branche master de notre repository. Cette pipelines pourra servir pour le déploiement de notre nouvelle application étant donné que les technologies employées seront les mêmes.

3: Travaux architecturaux:
Nous avons également pu réaliser des travaux de définition de l'architecture de l'API de notre PoC qui pourront être utiles
