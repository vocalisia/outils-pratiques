# Écart entre deux scénarios de frais annuels

Isoler l'effet arithmétique de deux niveaux de frais, à hypothèses de rendement identiques.

Ressource associée à [boursier.ch](https://boursier.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py fee_difference resources/boursier-ch-ecart-frais/exemple-fictif.json
```

## Informations à conserver

- Hypothèse.
- Capital initial.
- Rendement hypothétique décimal.
- Frais A décimaux.
- Frais B décimaux.
- Durée années.
- Source tarifaire.

## Méthode et limites

La fonction `fee_difference` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Rendement constant et frais annuels simplifiés ; ce calcul n'est pas une prévision et ne représente aucun produit réel.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
