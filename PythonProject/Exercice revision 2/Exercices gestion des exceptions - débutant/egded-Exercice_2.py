def permuter_elements_liste(liste, i, j):
    """
    Cette fonction permet de permuter 2 éléments d'une
    liste étant donné leurs indices.
    :param liste: La liste sur laquelle on veut faire la permutation.
    :param i: L'indice de l'élément à permuter.
    :param j: L'indice de l'autre élément à permuter.
    :return: La liste avec les deux éléments permutés.
    """
    try:
        liste[i], liste[j] = liste[j], liste[i]
    #except IndexError:
     #   print("Indice doit faire partie de la liste")
      #  return liste

    finally:
        print("good")

if __name__ == "__main__":
    liste = ["abc"]
    print(f"La liste d'origine est {liste}")

    indice1 = 0
    indice2 = 2

    print(f"Permutation des éléments aux indices {indice1} et {indice2} en cours...")

    liste_perm = permuter_elements_liste(liste=liste, i=indice1, j=indice2)

    if liste_perm is not None:
        print(f"La liste avec les éléments permutés est {liste_perm}")