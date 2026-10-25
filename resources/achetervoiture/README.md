# Budget de détention d'une voiture

Comparer un achat sur une durée donnée en séparant prix d'achat, frais initiaux, dépenses mensuelles et revente hypothétique.

Ressource associée à [achetervoiture.be](https://achetervoiture.be/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py car_budget resources/achetervoiture/exemple-fictif.json
```

## Informations à conserver

- Poste.
- Montant observé.
- Devise.
- Période.
- Source du devis.
- Vérifié le.

## Méthode et limites

La fonction `car_budget` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucune taxe, valeur de revente ou assurance n'est préremplie comme montant réel. Tous les chiffres d'exemple sont fictifs.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.

## Référence

[Source à consulter](https://www.belgium.be/fr/mobilite/vehicules/acheter_ou_vendre_un_vehicule/acheter_d_occasion)
