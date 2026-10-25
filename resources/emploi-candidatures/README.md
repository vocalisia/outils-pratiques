# Suivi de candidatures et d'offres réelles

Suivre des candidatures distinctes et vérifier qu'une offre est encore disponible avant de postuler.

Ressource associée à [job-emploi.ch](https://job-emploi.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py application_summary resources/emploi-candidatures/exemple-fictif.json
```

## Informations à conserver

- Référence de candidature.
- Employeur vérifié.
- URL de l'offre.
- Date de candidature.
- Étape DRAFT / APPLIED / INTERVIEW / OFFER / CLOSED.
- Prochaine action.
- Dernière vérification de l'offre.

## Méthode et limites

La fonction `application_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucune offre d'emploi n'est générée ; les références d'exemple ne représentent pas des postes ouverts.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
