
# Pseudo-code fonction trouver_plus_longue_serie_croissante_indices
# Entrée : ventes (liste de nombres)
# Sortie : sous-liste correspondant à la plus longue série croissante

# Si la longueur de ventes < 2
#     Retourner []

# Pour chaque vente dans ventes
#     Si vente < 0
#         Afficher message d'erreur et retourner []

# Initialiser debut_serie = 0        # indice de début de la série actuelle
# Initialiser debut_meilleure = 0    # indice de début de la meilleure série
# Initialiser fin_meilleure = 0      # indice de fin de la meilleure série

# Pour i allant de 1 à longueur de ventes - 1
#     Si ventes[i] <= ventes[i - 1]
#         # Série interrompue
#         Si (i - debut_serie) > (fin_meilleure - debut_meilleure)
#             debut_meilleure = debut_serie
#             fin_meilleure = i
#         debut_serie = i    # Nouvelle série commence

# Après la boucle
# Si (longueur de ventes - debut_serie) > (fin_meilleure - debut_meilleure)
#     debut_meilleure = debut_serie
#     fin_meilleure = longueur de ventes

# Si (fin_meilleure - debut_meilleure) < 2
#     Retourner []

# Retourner ventes[debut_meilleure:fin_meilleure]   # sous-liste de la meilleure série

def trouver_plus_longue_serie_croissante(ventes):
    """
    Trouve la plus longue période de ventes croissantes
    en utilisant uniquement les indices.
    :param ventes: Liste de nombres (revenus quotidiens)
    :return: La liste correspondant à la plus longue série croissante
    """
    if len(ventes) < 2:
        return []

    for v in ventes:
        if v < 0:
            print("Impossible de calculer la série. Les ventes ne doivent pas être négatives.")
            return []

    # Indices pour la série actuelle
    debut_serie = 0
    # Indices pour la meilleure série trouvée
    debut_meilleure = 0
    fin_meilleure = 0

    for i in range(1, len(ventes)):
        if ventes[i] <= ventes[i - 1]:
            # Série interrompue, vérifier si c'est la meilleure
            if (i - debut_serie) > (fin_meilleure - debut_meilleure):
                debut_meilleure = debut_serie
                fin_meilleure = i
            # Commencer une nouvelle série
            debut_serie = i

    # Vérifier la dernière série à la fin de la liste
    if (len(ventes) - debut_serie) > (fin_meilleure - debut_meilleure):
        debut_meilleure = debut_serie
        fin_meilleure = len(ventes)

    # Si la meilleure série a moins de 2 éléments, retourner []
    if (fin_meilleure - debut_meilleure) < 2:
        return []

    # Retourner la sous-liste correspondant à la meilleure série
    return ventes[debut_meilleure:fin_meilleure]

# Pseudo-code fonction moyennes_ventes_par_periode_slicing
# Entrées :
#    ventes : liste de nombres
#    periode : nombre de jours
# Sortie : ventes_par_periode : liste des moyennes par période
#
# Si periode <= 0
#     Afficher message d'erreur et retourner []
#
# Pour chaque vente dans ventes
#     Si vente < 0
#         Afficher message d'erreur et retourner []
#
# Initialiser ventes_par_periode = []
#
# Pour i allant de 0 à longueur de ventes - periode, par pas de periode
#     tranche = ventes[i : i + periode]   # extraire une tranche de longueur 'periode'
#     moyenne = somme de tranche / periode
#     Ajouter moyenne à ventes_par_periode
#
# Retourner ventes_par_periode

def moyennes_ventes_par_periode(ventes, periode):
    """
    Permet de calculer les moyennes des ventes par
    période donnée en paramètre et de les mettre dans une liste.
    :param ventes: La liste des ventes.
    :param periode: La période (en nombre de jours)
    :return:
    """
    if periode <= 0:
        print(f"Impossible de calculer les moyennes pour une période de {periode} jours.")
        return []

    for v in ventes:
        if v < 0:
            print("Impossible de calculer les moyennes des ventes. Les ventes ne doivent pas être négatives.")
            return []

    ventes_par_periode = []

    # Parcourir la liste par tranches de longueur 'periode'
    for i in range(0, len(ventes) - periode + 1, periode):
        tranche = ventes[i:i + periode]
        moyenne = sum(tranche) / periode
        ventes_par_periode.append(moyenne)

    return ventes_par_periode

def meilleure_periode(moyennes_ventes):
    """
    Retourne la période de la meilleure vente.
    Le numéro de la meilleure période de vente
    étant l'indice de l'élément de la liste +1.
    :param moyennes_ventes: La liste des moyennes des ventes
    :return: La meilleure période de vente
    """
    if not moyennes_ventes:
        return None

    max_moyenne = max(moyennes_ventes)
    indice_max = moyennes_ventes.index(max_moyenne) + 1

    return indice_max