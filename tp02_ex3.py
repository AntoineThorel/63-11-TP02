"""
    Programme permettant de savoir si un trajet ou une série de trajet sont réalisable par rapport
    au réservoir d'essence d'une voiture. Pour ce faire il faut spécifier une distance en kilometres
    et un nombre de passagers à bord(sans compte le conducteur).
    Indications:
        - Le véhicule a les caractéristiques suivantes :
            - Une consommation fixe de 5.0 litre pour 100km
            - Pour chaque personne ajoutée (le conducteur ne compte pas), l'essence utilisée augmente de 30%
              en rapport à la consommation normale
                - Exemple : pour 1 personne en plus du conducteur, la consommation vaut 1.3 fois la consommation normale
                            pour 2 personnes en plus du conducteur, la consommation vaut 1.6 fois la consommation normale
        - Lors de la saisie de la distance, si l'utilisateur met 0, le programme rempli le réservoir d'essence
          du véhicule
        - Lorsque qu'un voyage est réalisable, un message affiche le nombre de litres restants
        - Le programme se termine uniquement si une panne d'essence se produit. Si cela arrive,
          Un message affiche que la panne arrivera lors de ce trajet. Un second message affichera
          la distance parcourue avec tous les trajets.

"""
### Déclaration et  Initialisation des variables



### Séquence d'opération
