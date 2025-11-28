def generer_paquet_carte() -> list:
    """
    Fonction qui crée toutes les cartes d'un paquet de cartes selon les valeurs et suites que l'on veut avoir

    :return: Le paquet de carte généré
    """
    # TODO: Trouver les bons paramètres de cette fonction et compléter le code.

def definir_carte_a_piger():
    """
    Fonction qui sélectionne aléatoirement une carte d'un paquet qui deviendra la cible à obtenir pour gagner.

    :return: La carte pigée
    """
    # TODO: Trouver les bons paramètres de cette fonction et compléter le code.
    #       Indice : Quelle fonction du module random permet de faire un choix aléatoire dans une collection (liste) ?
    pass

def simuler_partie_cartes():
    """
    Fonction qui mélange les cartes et fait ensuite la pige aléatoire des cartes une après l'autre
    en indiquant quel joueur est en train de piger. Lorsque la carte pigée est la même que la cible,
    le jeu se termine et le joueur qui a pigé est déclaré vainqueur.


    :return: Aucune valeur de retour
    """
    # TODO: Trouver les bons paramètres de cette fonction et compléter le code.
    #       Indices : Quelle fonction du module random mélange une collection (liste) ?
    #                 Comment peut on faire suspendre l'exécution de notre programme avec le module time ?


if __name__ == '__main__':
    suites_paquet = ["Pique", "Coeur", "Trèfle", "Carreau"]
    valeurs_paquet = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Reine", "Roi"]

    # TODO: Tous les appels aux fonctions sont là mais il manque les bonnes valeurs à envoyer en paramètres.

    paquet_cartes = generer_paquet_carte()

    for carte in paquet_cartes:
        print(carte)

    carte_cible = definir_carte_a_piger()

    simuler_partie_cartes()
