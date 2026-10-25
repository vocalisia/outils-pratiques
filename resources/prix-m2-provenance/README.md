# Provenance des indicateurs immobiliers

Conserver unité, périmètre et date avant de rapprocher deux indicateurs au mètre carré.

Ressource associée à [prix-m2-suisse.ch](https://prix-m2-suisse.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py evidence_summary resources/prix-m2-provenance/exemple-fictif.json
```

## Informations à conserver

- Indicateur.
- Valeur et unité.
- Périmètre géographique.
- Période.
- Biens et surface concernés.
- Source.
- État VERIFIED / MISSING / OUTDATED.
- Limite de comparaison.

## Méthode et limites

La fonction `evidence_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucun indice réel n'est fourni et un indicateur ne constitue pas une estimation individuelle.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
