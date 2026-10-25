# Contrôle local d'un sitemap XML

Distinguer sitemap d'URL et index de sitemaps, compter les entrées et repérer les doublons exacts hors ligne.

Ressource associée à [seo-true.com](https://seo-true.com/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py sitemap_audit resources/seo-true-sitemap/exemple-fictif.json
```

## Informations à conserver

- URL déclarée.
- Type d'entrée.
- Doublon exact.
- HTTP à vérifier.
- Canonical à vérifier.
- État Google à vérifier.

## Méthode et limites

La fonction `sitemap_audit` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucune URL n'est téléchargée et aucune indexation n'est inférée de sa présence dans le XML.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
