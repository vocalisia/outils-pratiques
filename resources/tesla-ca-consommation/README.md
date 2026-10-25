# Journal de consommation électrique observée

Ramener une mesure en kWh à 100 km en précisant si l'énergie vient de la batterie ou du compteur.

Ressource associée à [tesla-mag.ca](https://tesla-mag.ca/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py consumption resources/tesla-ca-consommation/exemple-fictif.json
```

## Informations à conserver

- Trajet fictif ou observé.
- Distance km.
- Énergie kWh.
- Énergie batterie ou compteur.
- Conditions et température.
- Date.
- Source de mesure.

## Méthode et limites

La fonction `consumption` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucune autonomie, efficacité hivernale ou performance d'un véhicule réel n'est affirmée à partir de l'exemple.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
