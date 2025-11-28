def simuler_attaque(j1: dict, j2: dict):
    """
    Simuler une attaque entre 2 joueurs
    :param j1: dictionnaire de stats du joueur 1
    :param j2: dictionnaire de stats du joueur 2
    :return:
    """
    dict_stats_j1["PV"] -= dict_stats_j2["Attaque"] # si (attaque - défense) > 0
    dict_stats_j2["PV"] -= dict_stats_j1["Attaque"] # pv = -(attaque

dict_stats_j1 = {
    "Attaque" : 5,
    "PV" : 100
}

dict_stats_j2 = {
    "Attaque" : 3,
    "PV" : 100
}
# TODO faire une boucle pour plusieurs attaques avec des valeurs aléatoires
# boucle infinie
    # généner attaque aléatoire pour chaque jouer
    # mettres les valeurs d'attaques dans les dictionnaires
    # appeler la fonction
    # afficher l'état du jeu
    # si un joueur 0 PV ou moins, terminer
dict_stats_j3 = dict_stats_j1 # pas une copie, ça reste le même dictionnaire
dict_stats_j4 = dict_stats_j2.copy() # .copy() : créer un nouveau dictionnaire et copier les valeurs
print(dict_stats_j1,dict_stats_j2)
simuler_attaque(dict_stats_j1,dict_stats_j2)
print(dict_stats_j1,dict_stats_j2)
print(dict_stats_j3) # oups le j3 a été attaqué en même temps que le j1 car c'est le même j1
print(dict_stats_j4)
