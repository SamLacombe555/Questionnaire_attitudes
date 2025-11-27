with open("produits.txt", "r") as fichier:
    contenu = fichier.read().splitlines()

print("Contenu complet :")
print(contenu)

with open("demo_liste_2.txt", "r") as fichier:
    contenu = fichier.read().split(",")

print("Fruits :")
print(contenu)
print(len(contenu))

with open("demo_dict.txt", "r") as fichier:
    contenu = fichier.read().splitlines()



print("Capitales :")
print(contenu)
dict_capitales = {}
for item in contenu:
    list_item = item.split(" : ")
    dict_capitales[list_item[0]] = list_item[1]
print(dict_capitales)
print(len(dict_capitales))