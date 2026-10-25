# Complétude d'une qualification commerciale

Séparer information connue et information manquante avant une revue humaine.

Ressource associée à [lead-gene.ch](https://lead-gene.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py qualification resources/leadgene-ch-qualification/exemple-fictif.json
```

## Informations à conserver

- Adéquation au marché.
- Problème confirmé.
- Rôle compris.
- Moment connu.
- Prochaine étape convenue.
- Source retrouvable.

## Méthode et limites

La fonction `qualification` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

La complétude ne prédit pas une vente et ne vaut pas autorisation de contact. Un NON documenté reste une information connue.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.

## Référence

[Source à consulter](https://lead-gene.ch/qualification-leads-b2b-suisse)
