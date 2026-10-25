# Contrat de fonctionnement d'un agent métier

Décrire ce qu'un agent doit produire, dans quelles conditions, et qui reprend une exception.

Ressource associée à [agents-ia.pro](https://agents-ia.pro/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py evidence_summary resources/agents-ia-recette/exemple-fictif.json
```

## Informations à conserver

- Tâche métier.
- Déclencheur.
- Entrées minimales.
- Sortie attendue.
- Exception.
- Responsable humain.
- Preuve.
- État VERIFIED / MISSING / OUTDATED.

## Méthode et limites

La fonction `evidence_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Une fiche complétée ne certifie ni autonomie, ni conformité, ni performance de l'agent.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
