# Preuves utiles pour comparer des entreprises

Distinguer une déclaration commerciale, une preuve consultée et une question non résolue.

Ressource associée à [trustrewiews.ch](https://trustrewiews.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py evidence_summary resources/trustrewiews-preuves/exemple-fictif.json
```

## Informations à conserver

- Entreprise dans copie privée.
- Critère.
- Déclaration reçue.
- Source indépendante éventuelle.
- Date de la preuve.
- État VERIFIED / MISSING / OUTDATED.
- Question ouverte.

## Méthode et limites

La fonction `evidence_summary` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Le registre ne crée pas d'avis, de note agrégée ou de recommandation d'entreprise. VERIFIED signifie seulement que l'utilisateur a consulté sa preuve.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
