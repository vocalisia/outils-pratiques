# Budget de frais de transaction

Additionner les frais fixes, proportionnels et annuels d'un scénario défini par l'utilisateur.

Ressource associée à [boursier.be](https://boursier.be/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py trading_fees resources/boursier-be-frais/exemple-fictif.json
```

## Informations à conserver

- Intermédiaire.
- Nombre d'ordres.
- Montant par ordre.
- Frais fixes.
- Taux proportionnel décimal.
- Autres frais annuels.
- Source et date.

## Méthode et limites

La fonction `trading_fees` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Ni impôt, ni rendement, ni cours actuel, ni recommandation d'investissement ne sont calculés. Une grille tarifaire réelle reste nécessaire.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
