# Revue d'une démonstration de vente IA

Contrôler la compréhension du besoin et la démonstration d'une fonction sans transformer l'exercice en promesse de revenu.

Ressource associée à [master-seller.fr](https://master-seller.fr/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py test_summary resources/master-seller-demonstration/exemple-fictif.json
```

## Informations à conserver

- Compétence observée.
- Situation fictive.
- Critère d'acceptation.
- Observation.
- Statut PASS / FAIL / NOT_RUN.
- Correction à préparer.

## Méthode et limites

La fonction `test_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Ce journal ne certifie pas une qualification professionnelle et ne promet aucune vente.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
