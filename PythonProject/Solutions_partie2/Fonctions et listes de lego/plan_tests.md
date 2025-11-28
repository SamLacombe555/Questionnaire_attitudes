1

| Cas | Description             | Entrée                  | Sortie attendue |
| --- | ----------------------- | ----------------------- | --------------- |
| 1   | Attaque > défense       | vie=100, def=10, atk=30 | 80              |
| 2   | Attaque = défense       | vie=50, def=20, atk=20  | 50              |
| 3   | Attaque < défense       | vie=70, def=40, atk=10  | 70              |
| 4   | Résultat de vie négatif | vie=10, def=0, atk=50   | 0               |
| 5   | Vie déjà faible         | vie=1, def=0, atk=5     | 0               |


2

| Cas | Description                      | Entrée                            | Sortie attendue |
| --- | -------------------------------- | --------------------------------- | --------------- |
| 1   | Couleur présente plusieurs fois  | ["rouge","bleu","rouge"], "rouge" | 66.66...        |
| 2   | Couleur présente une fois        | ["vert","bleu","rouge"], "bleu"   | 33.33...        |
| 3   | Couleur absente                  | ["rouge","bleu"], "vert"          | 0               |
| 4   | Liste vide                       | [], "rouge"                       | 0               |
| 5   | Toutes les briques de la couleur | ["jaune","jaune"], "jaune"        | 100             |

3

| Cas | Description                    | Entrée                         | Sortie attendue |
| --- | ------------------------------ |--------------------------------| --------------- |
| 1   | Plusieurs couleurs différentes | ["rouge","bleu","bleu","rouge"]| 2.0             |
| 2   | Toutes mêmes couleurs          | ["jaune","jaune","jaune"]      | 3.0             |
| 3   | Une seule couleur              | ["rouge"]                      | 1.0             |
| 4   | Liste vide                     | []                             | 0.0             |
