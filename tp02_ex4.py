import random

"""
    Programme simulant un jeu de BlackJack avec des lancés de dés. L'objectif du jeu est d'arriver au plus proche de
    21 sans dépasser 21. Pour se faire l'utilisateur peut lancer un nombre de dés de son choix. Le programme simule un
    lancer de dés (en générant aléatoirement des valeurs entre 1 et 6) et obtiens une somme. L'utilisateur peut décider
    de continuer de lancer des dés supplémentaires ou de s'arrêter (entrer 0 lorsque l'on demande le nombre de dés).
    L'ordinateur joue également en parallèle avec sa propre somme et son score est affiché également. Le jeu se termine lorsque le
    joueur ET l'ordinateur ont terminé de jouer.

    Indications:
        - Si le joueur entre 0 comme nombre de dés à lancer, cela signifie qu'il arrête de lancer plus de dés et sa partie se termine
        - Voici le détail sur la stratégie de jeu de l'ordinateur:
            - Si la somme de l'ordinateur est inférieure à 6, il demande 3 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 6 et inférieure à 12, il demande 2 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 12 et inférieure à 18, il demande 1 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 18, il s'arrête de jouer

"""
### Déclaration et Initialisation des variables
joueurlance: int = None
ordilance: int = None
joueurscore: int = None
ordiscore: int = None
joueurfin: bool = False
ordifin: bool = False
joueurscore = 0
ordiscore = 0
### Séquence d'opération
while (not joueurfin) or not ordifin:
    if joueurfin == False:
        joueurlance = int(input("Combien de dés souhaitez-vous lancer ? "))
        for nb in range (0, joueurlance):
            joueurscore += random.randint(1,6)
        print("Vous avez un score de ", joueurscore)
    if ordifin == False:
        if ordiscore < 6:
            ordilance = 3
        elif ordiscore >= 6 and ordiscore < 12:
            ordilance = 2
        elif ordiscore >= 12 and ordiscore < 18:
            ordilance = 1
        else:
            ordilance = 0
        for nb in range(0, ordilance):
            ordiscore += random.randint(1, 6)
        if ordilance != 0:
            print("L'ordinateur choisi", ordilance, "dés")
            print("L'ordinateur a un score de ", ordiscore)
    if ordilance == 0:
        ordifin = True
    if joueurlance == 0 or joueurscore > 21:
        joueurfin = True
if (joueurscore <= 21 and ordiscore > 21) or (joueurscore <= 21 and (joueurscore - 21) > (ordiscore - 21)):
    print("Vous avez gagné (" + str(joueurscore) + ") contre l'ordinateur (" + str(ordiscore) + ")")
elif (ordiscore <= 21 and joueurscore > 21) or (ordiscore <= 21 and (ordiscore - 21) > (joueurscore - 21)):
    print("Vous avez perdu (" + str(joueurscore) + ") contre l'ordinateur (" + str(ordiscore) + ")")
elif (ordiscore == joueurscore) and (ordiscore <= 21):
    print("Vous avez fait égalité (" + str(joueurscore) + ") avec l'ordinateur (" + str(ordiscore) + ")")
else:
    print("Il n'y a aucun gagnant")
