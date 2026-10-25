# Addition de postes d'un devis de travaux

Recalculer des lignes quantité × prix et isoler les forfaits avant de comparer des périmètres équivalents.

Ressource associée à [meilleurartisan.ch](https://meilleurartisan.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py quote_total resources/artisan-devis/exemple-fictif.json
```

## Informations à conserver

- Lot et périmètre.
- Unité.
- Quantité.
- Prix unitaire du devis réel.
- Exclusions.
- Forfait complémentaire.
- Date et référence du devis.

## Méthode et limites

La fonction `quote_total` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Les chiffres ne sont pas des prix de marché. Aucune TVA, garantie ou subvention n'est supposée.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
