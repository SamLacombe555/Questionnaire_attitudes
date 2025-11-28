liste_pourcentage = []
def pourcentage():
    for i in range(8):
        liste_pourcentage.append(str(input("ajouter un lego avec une couleur")))
    choix_couleur_1 = str(input("quelle couleur est que vous voulez trouvez son pourcentage avec?")).strip()
    montant_lego_choisi = (len(choix_couleur_1) -1)
    lego_total = len(liste_pourcentage)
    pourcentage_couleur = 100*montant_lego_choisi/lego_total
    return f"{pourcentage_couleur: .2f}%"

print(pourcentage())
