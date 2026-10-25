# Bilan de temps et de coût d'une automatisation

Distinguer le temps net économisé, le coût récurrent et un délai de récupération purement calculé.

Ressource associée à [iapmesuisse.ch](https://iapmesuisse.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py automation_balance resources/iapme-temps-net/exemple-fictif.json
```

## Informations à conserver

- Processus.
- Minutes nettes économisées par exécution.
- Exécutions mensuelles.
- Coût horaire choisi.
- Coût mensuel outil.
- Mise en place.
- Preuve de mesure.

## Méthode et limites

La fonction `automation_balance` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Le calcul suppose des gains répétables, des coûts stables et aucun autre coût ; les montants d'exemple sont fictifs.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
