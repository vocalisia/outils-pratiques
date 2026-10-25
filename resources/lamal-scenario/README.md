# Budget annuel sous hypothèses choisies

Additionner douze primes et un reste à charge explicitement choisi, sans prétendre calculer le remboursement réel.

Ressource associée à [sante-lamal.ch](https://sante-lamal.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py annual_scenario resources/lamal-scenario/exemple-fictif.json
```

## Informations à conserver

- Contrat ou variante.
- Prime mensuelle vérifiée.
- Année de la prime.
- Reste à charge choisi pour le scénario.
- Source officielle.
- Hypothèses à vérifier.

## Méthode et limites

La fonction `annual_scenario` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Ce modèle indépendant n'est pas Priminfo et ne recommande pas de franchise. Il ne calcule pas les prestations d'assurance ou les dépenses de santé.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.

## Référence

[Source à consulter](https://www.bag.admin.ch/fr/priminfo-le-calculateur-de-primes-officiel-de-la-confederation)
