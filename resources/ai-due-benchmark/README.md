# Comparaison de tâches manuelles et automatisées

Mesurer le temps net en comptant la relecture et la fréquence, avec les mêmes critères de résultat.

Ressource associée à [ai-due.com](https://ai-due.com/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py time_comparison resources/ai-due-benchmark/exemple-fictif.json
```

## Informations à conserver

- Tâche.
- Durée manuelle min.
- Durée automatisée min.
- Relecture min.
- Résultat accepté.
- Conditions d'essai.
- Trace.

## Méthode et limites

La fonction `time_comparison` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Les durées d'exemple sont inventées. Aucun gain réel ou revenu n'est déduit d'un exemple.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
