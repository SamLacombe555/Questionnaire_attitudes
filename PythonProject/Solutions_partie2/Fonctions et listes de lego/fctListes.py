# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et
les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""
def points_de_vie_restants(vie: int, defense: int, attaque: int) -> int:
    """
    Calcule les points de vie restants après une attaque.

    :param vie: Points de vie actuels du joueur.
    :param defense: Points de défense du joueur attaqué.
    :param attaque: Points d'attaque de l'adversaire.
    :return: Points de vie restants (minimum 0).
    """
    degats = attaque - defense
    if degats < 0:
        degats = 0
    vie_restante = vie - degats
    if vie_restante < 0:
        vie_restante = 0
    return vie_restante

"""
2. Fonction qui reçoit une liste de legos et une couleur et 
qui retourne le pourcentage de blocs de cette couleur
"""
def pourcentage_couleur(legos: list, couleur: str) -> float:
    """
    Retourne le pourcentage de blocs d'une couleur donnée.

    :param legos: Liste contenant les couleurs des blocs (ex: ["rouge", "bleu", "rouge"]).
    :param couleur: Couleur recherchée.
    :return: Pourcentage de blocs de cette couleur (entre 0 et 100).
    """
    if not legos:
        return 0.0
    nb_couleur = 0
    for bloc in legos:
        if bloc == couleur:
            nb_couleur += 1
    return (nb_couleur / len(legos)) * 100

"""
3. Fonction qui reçoit une liste de legos et 
qui retourne il y a combien de blocs de chaque couleur en moyenne
"""
def moyenne_blocs_par_couleur(legos: list) -> float:
    """
    Retourne le nombre moyen de blocs par couleur.

    :param legos: Liste contenant les couleurs des blocs.
    :return: Moyenne de blocs par couleur.
    """
    if not legos:
        return 0.0

    couleurs_uniques = []
    for bloc in legos:
        if bloc not in couleurs_uniques:
            couleurs_uniques.append(bloc)

    return len(legos) / len(couleurs_uniques)

# Répartition des tâches :
"""                     
a   b   c
1   2   3   Nom :                   
2   3   1   Nom :                   
3   1   2   Nom :                   
"""