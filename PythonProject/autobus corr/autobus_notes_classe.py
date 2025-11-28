def simuler_attaque(j1: dict, j2: dict):
    """
    Simuler une attaque entre 2 joueurs
    :param j1: dictionnaire de stats du joueur 1
    :param j2: dictionnaire de stats du joueur 2
    :return:
    """


    j1["PV"] -= j2["Attaque"]
    j2["PV"] -= j1["Attaque"]
    return j1, j2

dict_stats_j1 = {
    "Attaque" : 5,
    "PV" : 100
}

dict_stats_j2 = {
    "Attaque" : 3,
    "PV" : 100
}