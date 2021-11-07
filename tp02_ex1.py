"""
Considérons les opérations suivantes applicables à un nombre entier (positif) :
    — si ce nombre est divisible par 3, on lui ajoute 4 ;
    — s’il n’est pas divisible par 3 mais divisible par 4, on le divise par 2;
    — s’il n’est divisible ni par 3, ni par 4, on lui soustrait 1.
On répète ces opérations successivement jusqu’à arriver à 0.

Ecrivez un programme affichant le nombre d'opérations pour arriver à 0 pour
chaque chiffre entier compris entre deux valeurs demandées à l'utilisateur.

"""

###Déclaration et Initialisation des variables
chiffre_1: int = None
chiffre_2: int = None
nb_ops: int = 0
var: int = None
chiffre_1 = int(input("Choisissez un chiffre de départ "))
chiffre_2 = int(input("Choisissez un chiffre de fin "))
### Séquence d'opération
for nb in range(chiffre_1, chiffre_2 + 1):
    var = nb
    while var != 0:
        if var % 3 == 0:
            var += 4
        elif var % 4 == 0:
            var = var / 2
        else:
            var -= 1
        nb_ops += 1
    print (str(nb) + " -> " + str(nb_ops))
    nb_ops = 0
