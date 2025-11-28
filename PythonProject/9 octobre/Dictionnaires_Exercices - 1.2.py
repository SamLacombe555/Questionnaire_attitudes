
def choix():
    choisi = int(input("1 - Créer \n2 - Modifier existant \n3 - Supprimer existant \n4 - Afficher existants"))

    if choisi == 1:
        key_ajoute = str(input("Quelle clé est-ce qu'on ajoute?"))
        value_ajoute = str(input("Quelle valeur est-ce qu'on lui donne?"))
        dict_ordi[key_ajoute] = value_ajoute
        print(f"La clé '{key_ajoute}' s'est fait ajouter avec la valeur '{value_ajoute}'")

    if choisi == 2:
        key_ajoute = str(input("Quelle clé est-ce qu'on modifie?"))
        value_ajoute = str(input("Quelle valeur est-ce qu'on lui donne?"))
        dict_ordi[key_ajoute] = value_ajoute
        print(f"La clé '{key_ajoute}' s'est fait modifier avec sa nouvelle valeur de '{value_ajoute}'")

    if choisi == 3:
        key_supprime = str(input("Quelle clée est-ce qu'on supprime?"))
        del dict_ordi[key_supprime]
        print(f"La clée '{key_supprime}' s'est fait supprimer")

    if choisi == 4:
        print("")
        for key, value in dict_ordi.items():
            print(f"{key:<15} {value}")
        print("")
dict_ordi = {
    "Carte graphique" : "2 Go",
    "RAM" : "32 Go",
    "Carte réseau" : "1000 Mbps"
}
while True:
    choix()

