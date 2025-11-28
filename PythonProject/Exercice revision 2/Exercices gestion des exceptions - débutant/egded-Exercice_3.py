def trier_liste(liste):
    try:
        liste.sort()

    except AttributeError:
        print("")
    finally:
        print("")

if __name__ == "__main__":
    liste_nums = [6, 3, 5, 2, 4, 1]
    trier_liste(liste_nums)
    print(liste_nums)
