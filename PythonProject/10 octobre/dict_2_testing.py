import random

def simuler_attaque_rd(j1: dict, j2: dict):
    """
    Simuler une attaque entre 2 joueurs avec des valeurs alléatoires
    :param j1: dictionnaire de stats du joueur 1
    :param j2: dictionnaire de stats du joueur 2
    :return:
    """
    j1["Attaque"] = random.choice(liste_attaque)
    j2["Attaque"] = random.choice(liste_attaque)

    j1["PV"] -= j2["Attaque"]
    j2["PV"] -= j1["Attaque"]

liste_attaque = [1,2,3,4,5]

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
while dict_stats_j1["PV"] > 0 and dict_stats_j2["PV"] > 0:
    simuler_attaque_rd(dict_stats_j1,dict_stats_j2)
    print(dict_stats_j1,dict_stats_j2)
print("fini")
if dict_stats_j1["PV"] <= 0:
    print("Joueur 2 gagne!")
else:
    print("Joueur 1 gagne!")
    # généner attaque aléatoire pour chaque jouer
    # mettres les valeurs d'attaques dans les dictionnaires
    # appeler la fonction
    # afficher l'état du jeu
    # si un joueur 0 PV ou moins, terminer
