# Journal des pièces et des échanges d'une facture

Retrouver les pièces et l'historique sans inventer de délai applicable ou de démarche automatique.

Ressource associée à [recouvrementpro.ca](https://recouvrementpro.ca/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py evidence_summary resources/recouvrement-journal/exemple-fictif.json
```

## Informations à conserver

- Référence anonymisée.
- Événement.
- Date réelle.
- Pièce ou preuve privée.
- Réponse obtenue.
- Juridiction à confirmer.
- État VERIFIED / MISSING / OUTDATED.
- Décision humaine.

## Méthode et limites

La fonction `evidence_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucune relance n'est envoyée et aucune procédure, juridiction ou prescription n'est déterminée.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
