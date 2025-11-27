with open("produits.txt", "r") as fichier:
    contenu = fichier.read().splitlines()

print("Contenu complet :")
print(contenu)

#TODO : transformer demo_liste_2.txt en liste
with open("demo_liste_2.txt", "r") as fichier:
    contenu = fichier.read().split(",")

print("Fruits :")
print(contenu)
print(len(contenu))

