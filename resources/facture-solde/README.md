# Solde arithmétique d'une facture et de ses paiements

Rapprocher des paiements d'une facture en séparant solde restant et éventuel trop-perçu.

Ressource associée à [xn--factureimpaye-mhb.fr](https://xn--factureimpaye-mhb.fr/), avec affiliation explicite. Il ne s'agit pas d'un avis indépendant sur ce site.

## Téléchargements

- [Classeur Excel](modele.xlsx) : consignes, journal de saisie, entrées fictives et exemple calculé.
- [Trame CSV](trame.csv), importable dans une copie privée de Sheets.
- [Scénario JSON fictif](exemple-fictif.json) et [sortie calculée](resultat-exemple.json).

Le classeur ne contient pas de formules de recalcul automatique. Pour refaire le calcul, téléchargez le projet complet, modifiez une copie privée du scénario JSON et lancez depuis le dossier du projet :

```text
python -X utf8 run.py invoice_balance resources/facture-solde/exemple-fictif.json
```

## Informations à conserver

- Référence anonymisée.
- Montant de facture.
- Paiement reçu.
- Date réelle.
- Justificatif privé.
- Solde à rapprocher.
- Litige ou question à traiter.

## Méthode et limites

La fonction `invoice_balance` est disponible dans [calculations.py](../../calculations.py) avec ses [tests automatisés](../../test_calculations.py). Le scénario fourni a été exécuté pendant la construction du paquet. Les états ou nombres d'exemple ne sont pas des observations de clients ou de produits.

Aucun intérêt, indemnité, frais de justice, prescription ou droit au recouvrement n'est calculé.

Les calculs utilisent des nombres à virgule flottante arrondis à six décimales ; ce n'est pas un logiciel de tenue comptable. Les unités et devises doivent être cohérentes. Les données réelles restent dans votre copie privée, jamais dans le dépôt public ou ses issues.
