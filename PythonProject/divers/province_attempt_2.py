# Les provinces associées à leur capitale.
#from PythonProject.Solutions_partie2.iles import indince

provinces = {
"Yukon"                : "Whitehorse",
"TNO"                  : "Yellowknife",
"Nunavut"              : "Iqaluit",
"Terre-Neuve"          : "St-John's",
"IPE"                  : "Charlottetown",
"Nouvelle-Écosse"      : "Halifax",
"Nouveau-Brunswick"    : "Fredericton",
"Québec"               : "Québec",
"Ontario"              : "Toronto",
"Manitoba"             : "Winnipeg",
"Saskatchewan"         : "Regina",
"Alberta"              : "Edmonton",
"Colombie-Britannique" : "Victoria"
}

import random

capitales = {}
for key, value in provinces.items():
    capitales[value] = key

Continue = True

points = 0
#PSEUDOCODE
#boucle du jeux
#   solution_item = choisi province.item par harsard
#   solution = random choice entre province et capitale
#   indice = autre choix
#   if solution == province
#       indice = capitale
#       guess = demande joueur quelle est la province en donnant la capitale
#       FONCTION qui vérifie la réponse du joueur et renvoye True ou False
#           if guess.lower == solution
#               return True
#           else return False
#

while Continue == True:
    choix_list = random.choice([provinces,capitales])
    if choix_list == provinces:
        indice = "province"
    else:
        indice = "capitale"
    solution_clee = random.choice(list(choix_list.keys()))
    guess = str(input(f"Quelle est la {indice} de {choix_list[solution_clee]}?"))
    if guess.lower() == solution_clee.lower():
        points += 1
    if guess =="":
        Continue = False

print(f"Tu as accumulé {points} points")
