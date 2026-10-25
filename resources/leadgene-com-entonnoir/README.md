# Conversions d'un entonnoir commercial

Calculer séparément réponse, rendez-vous, présence et vente sur une même cohorte.

Ressource associée à [lead-gene.com](https://lead-gene.com/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py funnel resources/leadgene-com-entonnoir/exemple-fictif.json
```

## Informations à conserver

- Cohorte et période.
- Contacts distincts.
- Réponses de la cohorte.
- RDV pris.
- RDV tenus.
- Ventes de la cohorte.
- Méthode de dédoublonnage.

## Méthode et limites

La fonction `funnel` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Le calcul exige un entonnoir emboîté et des unités identiques. Il ne convient pas aux étapes comptées sur des cohortes différentes.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
