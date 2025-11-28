"""
# demande joueur1 le nombre a deviner
#print \n *100
#fonction pour le jeux
    #set score
    #set boucle
        #


def deviner(a_trouver):

    score = 0
    trouvee = False

    while trouvee == False:
        guess = int(input("Que crois-tu es le nombre?"))

        if guess == a_trouver:
            trouvee == True

        elif guess != a_trouver:
            if guess >= a_trouver:
                print("Bonne essay, mais le nombre est plus petit")
            elif guess <= a_trouver:
                print("Bonne essay, mais le nombre est plus grand")
        score += 1

    print(f"Bravo! Tu as trouver le nombre en {score} essay.")
"""

def deviner_nombre(nombre_a_deviner:int):
    """
    Fonction qui permet de guider l'utilisateur
    à deviner un nombre passé en paramètres.
    :param nombre_a_deviner: Le nombre à deviner.
    :return: Aucun
    """

    score = 0
    trouve = False

    while not trouve:
        score += 1

        nombre_propose = int(input(f"Tentative {score}: Quel nombre tentez-vous? "))

        if nombre_propose == nombre_gagnant:
            trouve = True
        else:
            if nombre_propose < nombre_a_deviner:
                print("Le nombre est plus haut")
            else:
                print("Le nombre est plus petit")

    print("*******************************")
    print(f"Bravo! La bonne réponse était {nombre_gagnant}")
    print(f"Votre score est de {score}")


if __name__ == "__main__":
    nombre_gagnant = int(input("Quel est le nombre à faire deviner? "))
    print("\n" * 100)

    deviner_nombre(nombre_gagnant)
