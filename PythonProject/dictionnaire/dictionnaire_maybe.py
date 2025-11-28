dict_notes = {
    'Jacques' : 90,
    'Alice' : 67,
    'Charle' : 50,
    "Bob" : 80,
    "David" : 100
}
print(dict_notes)
dict_notes["Julie"] = 70 # Ajouter un item
dict_notes["Charle"] = 55 # Modifier un item
del dict_notes["David"] # Supprimer un item

for key, value in dict_notes.items(): # .items() : lignes du dictionnaire
    print(f"{key:<15} {value} %")

if "Bob" in dict_notes:
    print(dict_notes["Bob"])

noms = list(dict_notes.keys()) # liste des clés
notes = list(dict_notes.values()) # liste des valeurs
print(noms)
print(notes)
print("Moyenne:", sum(notes)/len(notes))
print("Nombre d'étudiants:", len(dict_notes))
nb_succes = 0
for i in range(len(dict_notes)):
    if list(dict_notes.values())[i] >= 60:
        nb_succes += 1
print("Nombre de succès : ", nb_succes)
nb_echec = 0
for cle, val in dict_notes.items():
    if val < 60:
        nb_echec += 1
print("Nombre d'échecs : ", nb_echec)

