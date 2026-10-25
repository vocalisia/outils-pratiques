# Contrôle local d'un document HTML

Lire titre, H1, langue, canonical et robots dans une chaîne HTML locale, sans requête réseau.

Ressource associée à [seo-swiss.ch](https://seo-swiss.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py html_audit resources/seo-swiss-html/exemple-fictif.json
```

## Informations à conserver

- URL observée.
- Date de capture.
- HTTP mesuré séparément.
- Titre.
- H1.
- Canonical déclaré.
- Robots déclaré.
- Vérification GSC distincte.

## Méthode et limites

La fonction `html_audit` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Le résultat n'est pas un rendu JavaScript, un test HTTP ou une preuve d'indexation. Les valeurs fournies viennent du seul document analysé.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
