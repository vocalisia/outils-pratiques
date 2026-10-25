# Puissance nominale d'un ensemble de panneaux

Convertir nombre × puissance nominale en kWc sans confondre puissance et production énergétique.

Ressource associée à [tesla-mag.ch](https://tesla-mag.ch/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py panel_power resources/tesla-ch-puissance/exemple-fictif.json
```

## Informations à conserver

- Référence du panneau.
- Nombre.
- Puissance nominale Wc par panneau.
- Puissance totale kWc.
- Fiche technique.
- Conditions à vérifier.

## Méthode et limites

La fonction `panel_power` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Le calcul ne donne ni kWh annuels, ni rendement, ni rentabilité ou dimensionnement professionnel.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
