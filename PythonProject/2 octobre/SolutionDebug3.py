def roche_papier_ciseau(choix_joueur1: str, choix_joueur2: str) -> None:
    """
    Compare les choix de deux joueurs au jeu Roche-Papier-Ciseau
    et affiche le gagnant ou si la partie est nulle.
    """
    armes = ["roche", "papier", "ciseau"]

    choix_joueur1 = choix_joueur1.lower()
    choix_joueur2 = choix_joueur2.lower()
    # Validation
    if choix_joueur1 not in armes or choix_joueur2 not in armes:
        print("Vous n'avez pas entré roche, papier ou ciseau. :(")
        return

    # Partie nulle
    if choix_joueur1 == choix_joueur2:
        print("Partie nulle!")
        return

    # Cas où joueur 1 gagne
    if ((choix_joueur1 == "roche" and choix_joueur2 == "ciseau")
            or (choix_joueur1 == "papier" and choix_joueur2 == "roche")
            or (choix_joueur1 == "ciseau" and choix_joueur2 == "papier")):
        joueur_gagnant = "joueur 1"
        arme_gagnante = choix_joueur1
    else:
        joueur_gagnant = "joueur 2"
        arme_gagnante = choix_joueur2

    #print(f"\nLe gagnant est {joueur_gagnant} avec {arme_gagnante}, félicitations!")
    return f"{joueur_gagnant} gagne avec {arme_gagnante}"

if __name__ == "__main__":
    print("""
    Bienvenue au jeu Roche-Papier-Ciseau.
    Veuillez faire un choix parmi les suivants : 
    roche
    papier
    ciseau
    """)

    choix1 = input("Choix du joueur 1 : ")
    choix2 = input("Choix du joueur 2 : ")

    resultat = roche_papier_ciseau(choix1, choix2)
    print(resultat)
