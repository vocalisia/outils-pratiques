# Planning d'aide non médicale

Répartir les créneaux d'aide quotidienne et calculer le total hebdomadaire sans information médicale.

Ressource associée à [assistanceseniors.ch](https://assistanceseniors.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py weekly_hours resources/assistance-planning/exemple-fictif.json
```

## Informations à conserver

- Jour.
- Créneau.
- Aide non médicale prévue.
- Durée min.
- Intervenant dans copie privée.
- Relais.
- Confirmé.

## Méthode et limites

La fonction `weekly_hours` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Ce planning ne définit pas un besoin de soins, une prescription ou l'éligibilité à une prestation.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
