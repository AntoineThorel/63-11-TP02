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
RESERVOIR: int = 32.5
CONSO: float = 5.0
distance: int = None
passagers: int = None
fin: bool = False
reste : float = 0.0
var: float = None
compteur: float = 0
### Séquence d'opération
var = RESERVOIR
while not fin:
    distance = int(input("Entrez la distance de votre destination ou entrez 0 pour faire le plein :"))
    if distance == 0:
        print("Le réservoir est rempli totalement")
        var = 32.5
    if distance != 0:
        passagers = int(input("Combien de personnes font parties du trajet en plus du conducteur ? "))
        if passagers == 0 and var >= 0:
            reste = var - distance * (CONSO / 100)
            if reste >= 0:
                print("Il vous reste encore " + str(reste) + "litres d'essence")
                compteur += distance
            var = reste
        elif passagers > 0 and var >= 0:
            reste = var - distance * (CONSO * (1 + 0.3 * passagers)) / 100
            if reste >= 0:
                print("Il vous reste encore " + str(reste) + "litres d'essence")
                compteur += distance
            var = reste
        if var < 0:
            fin = True
            print("Vous allez tomber en panne d'essence lors de ce trajet! Pensez à le raccourcir ou faire le plein. ")
            print("Vous aurez parcouru " + str(compteur) + "km")
