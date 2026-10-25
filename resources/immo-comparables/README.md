# Lecture arithmétique de comparables immobiliers

Calculer les prix par unité de surface et leur médiane tout en conservant la provenance des comparables.

Ressource associée à [estimation-bien.ch](https://estimation-bien.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py comparables resources/immo-comparables/exemple-fictif.json
```

## Informations à conserver

- Bien comparable.
- Prix observé.
- Surface et unité.
- Date d'observation.
- Type de surface.
- Localisation.
- Source.
- Différences à documenter.

## Méthode et limites

La fonction `comparables` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Une médiane de prix affichés n'est pas une valeur vénale. Aucune correction d'emplacement, de qualité ou de date n'est automatique.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
