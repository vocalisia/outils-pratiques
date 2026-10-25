# Comparaison reproductible d'outils sur une tâche

Tester des outils sur une même entrée avant de produire un classement dépendant du besoin.

Ressource associée à [trust-vault.com](https://trust-vault.com/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py test_summary resources/trust-vault-comparaison/exemple-fictif.json
```

## Informations à conserver

- Tâche commune.
- Outil et version.
- Entrée identique.
- Résultat attendu.
- Résultat observé.
- Statut PASS / FAIL / NOT_RUN.
- Temps et coût mesurés.
- Conditions.

## Méthode et limites

La fonction `test_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucun outil réel n'est noté dans les exemples. L'affiliation et les conditions d'essai doivent accompagner une comparaison publiée.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
