# 1. Liste simple
fruits = ["Pomme", "Banane", "Orange"]

with open("demo_liste.txt", "w") as f:
    f.writelines(fruits)

with open("demo_liste_2.txt", "w") as f:
    f.write(",".join(fruits))

with open("demo_liste_3.txt", "w") as f:
    f.write("\n".join(fruits))


# 2. Dictionnaire simple
capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}



# 3. Liste 2D (ex: grille)
notes = [
    [12, 15, 17],
    [14, 10, 18],
    [19, 11, 16]
]



# 4. Liste de dictionnaires (ex: élèves)
eleves = [
    {"nom": "Alice", "age": 14},
    {"nom": "Bob", "age": 15},
    {"nom": "Chloé", "age": 14}
]

# 5. Dictionnaire de listes (ex: matières -> notes)
bulletins = {
    "Math": [12, 14, 18],
    "Français": [15, 11, 16],
    "Histoire": [17, 10, 19]
}
