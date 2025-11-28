import random

def lancer_des():
    """Retourne la somme de deux dés."""
    return random.randint(1, 6) + random.randint(1, 6)

def jouer_craps():
    print("\n--- Nouvelle partie de Craps ---")
    input("Appuyez sur Entrée pour lancer les dés...")
    total = lancer_des()
    print(f"Premier lancer : {total}")

    if total in [7, 11]:
        print("Gagné immédiatement !")
        return
    elif total in [2, 3, 12]:
        print("Perdu immédiatement !")
        return
    else:
        point = total
        print(f"Le point est maintenant : {point}")
        while True:
            input("Relancer ? ")
            total = lancer_des()
            print(f"Résultat : {total}")
            if total == point:
                print("Vous avez regagné le point : Gagné !")
                return
            elif total == 7:
                print("Vous avez fait 7 avant le point : Perdu !")
                return

def boucle_jeu():
    while True:
        choix = input("Voulez-vous jouer une partie ? (o/n) : ").lower()
        if choix == "o":
            jouer_craps()
        else:
            print("Fin du jeu.")
            break

# Programme principal
boucle_jeu()
