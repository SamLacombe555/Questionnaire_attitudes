def progression_mot(mot: str, lettres_devinees: list) -> str:
    """
    Retourne la progression du mot à deviner en remplaçant
    les lettres non devinées par des tirets bas.
    """
    mot_actuel = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            mot_actuel += lettre
        else:
            mot_actuel += "_"
    return mot_actuel


def pendu() -> None:
    """
    Simule le jeu du Pendu. Le joueur doit deviner un mot.
    """
    max_essais = 6
    essais = 0
    mot_a_deviner = "python"
    lettres_devinees = []

    print("Bienvenue au jeu du Pendu!")

    etat_progression_mot = progression_mot(mot_a_deviner, lettres_devinees)

    while True:
        print("\nMot à deviner:", etat_progression_mot)
        lettre = input("Devinez une lettre : ").lower()

        if not lettre.isalpha() or len(lettre) != 1:
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_devinees:
            print("Vous avez déjà proposé cette lettre.")
            continue

        lettres_devinees.append(lettre)

        if lettre in mot_a_deviner:
            print("Bonne devinette!")
        else:
            print("Mauvaise devinette!")
            essais += 1

        etat_progression_mot = progression_mot(mot_a_deviner, lettres_devinees)

        if "_" not in etat_progression_mot:
            print(f"\nFélicitations, vous avez trouvé le mot {mot_a_deviner}!")
            print(f"Nombre d'essais erronés : {essais}")
            break

        if essais >= max_essais:
            print(f"\nVous avez épuisé vos {essais} essais ! Le mot était: {mot_a_deviner}")
            break


if __name__ == "__main__":
    pendu()
