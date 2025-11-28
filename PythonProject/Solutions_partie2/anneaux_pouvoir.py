# -----------------------------------------
# Simulateur de bataille - Les anneaux du pouvoir
# -----------------------------------------

def creer_armee_bien():
    """Crée et retourne la liste représentant l'armée de Galadriel."""
    # Format : [elfes, nains, humains]
    return [250, 150, 500]


def creer_armee_mal():
    """Crée et retourne la liste représentant l'armée de Sauron."""
    # Format : [trolls, worgs, orcs]
    return [100, 200, 2500]


def appliquer_strategie(armee_bien, armee_mal, strategie):
    """
    Modifie les listes selon la stratégie choisie :
    - 'agressive' : on enlève 500 orcs directement.
    - 'défensive' : on ajoute 175 nains en renfort.
    """
    if strategie == "agressive":
        # On retire 500 orcs au début
        # Position des orcs : index 2
        armee_mal[2] = armee_mal[2] - 500
        if armee_mal[2] < 0:
            armee_mal[2] = 0

    elif strategie == "défensive":
        # On ajoute 175 nains
        # Position des nains : index 1
        armee_bien[1] += 175

def calculer_force(armee):
    """
    Calcule la force de l'armée en unités "humains".

    Rappels :
    - Un elfe vaut la force de 10 humains
    - Un nain vaut la force de 5 humains
    - Un humain vaut 1 humain
    - Troll = elfe, donc force = 10 humains
    - Worg = nain, donc force = 5 humains
    - Orc = humain = 1 humain
    """

    force = armee[0] * 10 + armee[1] * 5 + armee[2]

    return force


def afficher_resultat(force_bien, force_mal):
    """Affiche le résultat final selon les forces totales."""
    if force_bien > force_mal:
        print("\nLa bataille est remportée et la paix pourra de nouveau régner.")
    else:
        print("\nLes forces du bien s'inclinent et la terre du milieu sombre dans le chaos.")


def simulateur_bataille():
    """Programme principal."""
    print("Bienvenu Galadriel, à votre simulateur de combat.")

    # Liste des stratégies
    strategies = ["agressive", "défensive"]

    choix = input("Quelle stratégie voulez-vous adopter [agressive, défensive] ? ").strip().lower()

    # Création des armées
    armee_bien = creer_armee_bien()
    armee_mal = creer_armee_mal()

    # Si le choix n'est pas reconnu, on affiche un message mais on peut tout de même arrêter
    if choix not in strategies:
        print("\nStratégie non reconnue. Le destin de la terre du milieu reste incertain...")

    else:
        # Appliquer la stratégie choisie
        appliquer_strategie(armee_bien, armee_mal, choix)

        # Calcul des forces
        force_bien = calculer_force(armee_bien)
        force_mal = calculer_force(armee_mal)

        # Affichage du verdict
        afficher_resultat(force_bien, force_mal)


# Lancement du programme
simulateur_bataille()
