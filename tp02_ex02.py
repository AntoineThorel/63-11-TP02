"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration et Initialisation des variables
prix_poulet : float = 4.90
prix_chips : float = 2.50
prix_choc : float = 2.00
prix_bonbon : float = 3.30
prix_tea : float = 2.20
prix_limonade : float = 1.90
cash2 : float = 0
fin: bool = False
fin2: bool = True
produit_choix: str = None
produit: int = None
promo: bool = False
rabais: float = 0.8
### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")
while not fin:
    produit_choix = input("Veuillez sélectionner un produit et votre offre promotionnelle :")
    produit = int(produit_choix[0])
    if produit_choix[2:6] == "#POU":
        promo = True
    if produit == 1 and not promo:
        print("Le prix à payer est de : " + str(prix_poulet))
        fin2 = False
    if produit == 1 and promo:
        prix_poulet = round(prix_poulet * rabais, 2)
        print("Le prix à payer est de : " + str(prix_poulet))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_poulet:
            print("Sandwich au poulet servi ! Bon appétit !")
            fin2 = True
        elif cash + cash2 >= prix_poulet:
            print("Sandwich au poulet servi ! Bon appétit !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_poulet, 2))
            fin2 = True
        else:
            print("Le montant est insuffisant. Veuillez ajouter encore : " + str(round(prix_poulet - (cash + cash2), 2)))
        cash2 += cash
    if produit == 2 and not promo:
        print("Le prix à payer est de : " + str(prix_chips))
        fin2 = False
    if produit == 2 and promo:
        prix_chips = round(prix_chips * rabais, 2)
        print("Le prix à payer est de : " + str(prix_chips))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_chips:
            print("Chips Paprika servies ! Bon appétit !")
            fin2 = True
        elif cash + cash2 >= prix_chips:
            print("Chips Paprika servies ! Bon appétit !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_chips, 2))
            fin2 = True
        else:
            print(
                "Le montant est insuffisant. Veuillez ajouter encore : " + str(round(prix_chips - (cash + cash2), 2)))
        cash2 += cash
    if produit == 3 and not promo:
        print("Le prix à payer est de : " + str(prix_choc))
        fin2 = False
    if produit == 3 and promo:
        prix_choc = round(prix_choc * rabais, 2)
        print("Le prix à payer est de : " + str(prix_choc))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_choc:
            print("Barre chocolatée servie ! Bon appétit !")
            fin2 = True
        elif cash + cash2 >= prix_choc:
            print("Barre chocolatée servie ! Bon appétit !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_choc, 2))
            fin2 = True
        else:
            print("Le montant est insuffisant. Veuillez ajouter encore : " + str(round(prix_choc - (cash + cash2), 2)))
        cash2 += cash
    if produit == 4 and not promo:
        print("Le prix à payer est de : " + str(prix_bonbon))
        fin2 = False
    if produit == 4 and promo:
        prix_bonbon = round(prix_bonbon * rabais, 2)
        print("Le prix à payer est de : " + str(prix_bonbon))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_bonbon:
            print("Bonbons servis ! Bon appétit !")
            fin2 = True
        elif cash + cash2 >= prix_bonbon:
            print("Bonbons servis ! Bon appétit !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_bonbon, 2))
            fin2 = True
        else:
            print(
                "Le montant est insuffisant. Veuillez ajouter encore : " + str(round(prix_bonbon - (cash + cash2), 2)))
        cash2 += cash
    if produit == 5 and not promo:
        print("Le prix à payer est de : " + str(prix_tea))
        fin2 = False
    if produit == 5 and promo:
        prix_tea = round(prix_tea * rabais, 2)
        print("Le prix à payer est de : " + str(prix_tea))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_tea:
            print("Ice Tea servi ! Santé !")
            fin2 = True
        elif cash + cash2 >= prix_tea:
            print("Ice Tea servi ! Santé !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_tea, 2))
            fin2 = True
        else:
            print("Le montant est insuffisant. Veuillez ajouter encore : " + str(round(prix_tea - (cash + cash2), 2)))
        cash2 += cash
    if produit == 6 and not promo:
        print("Le prix à payer est de : " + str(prix_limonade))
        fin2 = False
    if produit == 6 and promo:
        prix_limonade = round(prix_limonade * rabais, 2)
        print("Le prix à payer est de : " + str(prix_limonade))
        fin2 = False
    while not fin2:
        cash: float = float(input("Veuillez introduire votre monnaie :"))
        if cash + cash2 == prix_limonade:
            print("Limonade servie ! Santé !")
            fin2 = True
        elif cash + cash2 >= prix_limonade:
            print("Limonade servie ! Santé !")
            print("Monnaie à rendre : ", round(cash + cash2 - prix_limonade, 2))
            fin2 = True
        else:
            print("Le montant est insuffisant. Veuillez ajouter encore : " + str(
                round(prix_limonade - (cash + cash2), 2)))
        cash2 += cash
    if produit < 1 or produit > 6:
        print("Le produit sélectionné n'existe pas")
    if produit >= 1 and produit <= 6:
        fin = True
