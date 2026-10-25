# Matrice de décision pondérée

Comparer des options à critères et poids explicites, en conservant les preuves qui justifient chaque note.

Ressource associée à [suisy.ch](https://suisy.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py weighted_matrix resources/suisy-decision/exemple-fictif.json
```

## Informations à conserver

- Critère choisi.
- Poids choisi.
- Note option A entre 0 et 5.
- Preuve option A.
- Note option B entre 0 et 5.
- Preuve option B.
- Date.

## Méthode et limites

La fonction `weighted_matrix` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Les notes sont des choix de l'utilisateur, pas une mesure indépendante. Aucune marque n'est placée première automatiquement ; les égalités sont conservées.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
