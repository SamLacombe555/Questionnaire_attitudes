# Constante
CAPACITE_MAX = 50


def occuper_places(places_disponibles):
    """Demande un nombre de personnes à faire entrer et ajuste les places."""
    try:
        nb = int(input("Combien de personnes souhaitent entrer ? "))
        if nb < 0:
            print("Erreur. Le nombre doit être positif.")
            return places_disponibles

        if nb <= places_disponibles:
            print(f"{nb} personnes sont autorisées à entrer.")
            places_disponibles -= nb
        else:
            print(
                f"La capacité maximale du restaurant est atteinte. Uniquement {places_disponibles} personnes sont admises.")
            places_disponibles = 0

        print(f"Il reste {places_disponibles} places disponibles dans le restaurant.\n")
        return places_disponibles
    except ValueError:
        print("Erreur. Veuillez entrer un nombre entier.")
        return places_disponibles


def liberer_places(places_disponibles):
    """Demande un nombre de personnes à faire sortir et ajuste les places."""
    try:
        nb = int(input("Combien de personnes ont quitté le restaurant ? "))
        if nb < 0:
            print("Erreur. Le nombre doit être positif.")
            return places_disponibles

        places_occupees = CAPACITE_MAX - places_disponibles
        if nb > places_occupees:
            print(f"Erreur. Il y'a moins de {nb} personnes dans le restaurant.\n")
        else:
            print(f"{nb} personnes quittent le restaurant.")
            places_disponibles += nb
            print(f"Il reste {places_disponibles} places disponibles dans le restaurant.\n")

        return places_disponibles
    except ValueError:
        print("Erreur. Veuillez entrer un nombre entier.")
        return places_disponibles


def menu_principal():
    """Boucle principale du programme."""
    places_disponibles = CAPACITE_MAX

    while True:
        print("**************************************************************")
        print("************* Gestion des places au restaurant *************")
        print("**************************************************************")
        print(f"Le nombre de places disponibles : {places_disponibles}")
        print("Souhaitez-vous : ")
        print("\t 1. Occuper des places au restaurant.")
        print("\t 2. Libérer des places au restaurant.")
        print("\t 3. Quitter")
        print("**************************************************************")

        choix = input("Réponse : ").strip()

        if choix == "1":
            places_disponibles = occuper_places(places_disponibles)
        elif choix == "2":
            places_disponibles = liberer_places(places_disponibles)
        elif choix == "3":
            print("Au revoir.")
            break
        else:
            print("Action non valide. Veuillez choisir entre 1, 2 ou 3.\n")


# Lancer le programme
if __name__ == "__main__":
    menu_principal()
