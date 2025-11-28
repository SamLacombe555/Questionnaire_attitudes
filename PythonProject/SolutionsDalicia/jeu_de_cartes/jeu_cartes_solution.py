import random
import time

def generer_paquet_carte(suites: list, valeurs: list) -> list:
    """
    Fonction qui crée toutes les cartes d'un paquet de cartes selon les valeurs et suites que l'on veut avoir
    :param suites: Les suites du paquet de carte. Celles d'un paquet classique sont Coeur, Carreau, Trèfle et Pique
    :param valeurs: Les valeurs que les cartes peuvent prendre. Un paquet classique aura les valeurs de l'as au roi.
    :return: Le paquet de carte généré
    """

    paquet = []
    for suite in suites:
        for valeur in valeurs:
            paquet.append(f"{valeur} de {suite}")

    return paquet

def definir_carte_a_piger(paquet: list) -> str:
    """
    Fonction qui sélectionne une carte d'un paquet qui deviendra la cible à obtenir pour gagner
    :param paquet: Une liste qui contient toutes les cartes du paquet
    :return: La carte pigée
    """
    return random.choice(paquet)

def simuler_partie_cartes(paquet: list, cible: str):
    """
    Fonction qui mélange les cartes et fait ensuite la pige des cartes une après l'autre
    en indiquant quel joueur est en train de piger. Lorsque la carte pigée est la même que la cible,
    le jeu se termine et le joueur qui a pigé est déclaré vainqueur.
    :param paquet: Le paquet de carte avec lequel on joue
    :param cible: La carte à piger pour gagne
    :return: Aucune valeur de retour
    """
    print(f"La carte à piger pour gagner est : {cible}")
    time.sleep(1)
    random.shuffle(paquet)
    compteur = 0
    carte = ""
    while carte != cible:
        time.sleep(1)
        carte = paquet.pop(0)
        compteur += 1

        if compteur % 2 == 1:
            print(f"Le joueur 1 a pigé la carte : {carte}")
        else:
            print(f"Le joueur 2 a pigé la carte : {carte}")

    if compteur % 2 == 1:
        print("Le joueur 1 a pigé la carte cible en premier et remporte la partie!")
    else:
        print("Le joueur 2 a pigé la carte cible en premier et remporte la partie!")


if __name__ == '__main__':
    suites_paquet = ["Pique", "Coeur", "Trèfle", "Carreau"]
    valeurs_paquet = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi"]
    paquet_cartes = generer_paquet_carte(suites_paquet, valeurs_paquet)

    print(paquet_cartes)
    for carte in paquet_cartes:
        print(carte)

    cible = definir_carte_a_piger(paquet_cartes)

    simuler_partie_cartes(paquet_cartes, cible)