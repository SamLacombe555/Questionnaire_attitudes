import csv
import json

import notes
# 1. Liste simple


fruits = ["Pomme", "Banane", "Orange"]
with open("fruits.csv", "w") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(fruits)

with open("demo_liste.txt", "w") as f:
    f.writelines(fruits)

with open("demo_liste_2.txt", "w") as f:
    f.write(",".join(fruits))

with open("demo_liste_3.txt", "w") as f:
    f.write("\n".join(fruits))


# 2. Dictionnaire simple
capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}

with open("capitales.csv", "w", newline="") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=capitales.keys())
    writer.writeheader()
    writer.writerow(capitales)

with open("demo_dict.txt", "w") as f:
    for key, value in capitales.items():
        f.write(key + " : " + value + "\n")

#with open("capitales.json", "w")

# 3. Liste 2D (ex: grille)
notes = [
    [12, 15, 17],
    [14, 10, 18],
    [19, 11, 16]
]

with open("notes.csv", "w", newline="") as fichier:
    writer =csv.writer(fichier)
    writer.writerows(notes)

with open("demo_notes.txt", "w") as f:
    for ls_note in notes:
        f.write("\n")

with open("notes.json", "w", newline="") as f:
    json.dump(notes, f, ensure_ascii=False, indent=4)

# 4. Liste de dictionnaires (ex: élèves)
eleves = [
    {"nom": "Alice", "age": 14},
    {"nom": "Bob", "age": 15},
    {"nom": "Chloé", "age": 14}
]

with open("eleves.csv", "w", encoding="utf-8", newline="") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=eleves[0].keys())
    writer.writeheader()
    writer.writerows(eleves)

with open("eleves.json", "w", encoding="utf-8", newline="") as f:
    json.dump(eleves, f, ensure_ascii=False, indent=4)

# 5. Dictionnaire de listes (ex: matières -> notes)
bulletins = {
    "Math": [12, 14, 18],
    "Français": [15, 11, 16],
    "Histoire": [17, 10, 19]
}

with open("bulletins.json", "w", encoding="utf-8") as f:
    json.dump(bulletins, f, ensure_ascii=False, indent=4)
