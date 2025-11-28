# Tableau de tests – Fonction `trouver_plus_longue_serie_croissante`
| Cas de test                          | Entrée `ventes`               | Sortie attendue      | Justification                                                                                                              |
|--------------------------------------|-------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Liste vide                           | `[]`                          | `[]`                 | Aucun élément, donc aucune série possible                                                                                  |
| Un seul élément                      | `[5]`                         | `[]`                 | Une seule valeur ne peut pas former une série croissante                                                                   |
| Deux valeurs croissantes             | `[3, 7]`                      | `[3, 7]`             | Série croissante valide de longueur 2                                                                                      |
| Deux valeurs décroissantes           | `[10, 2]`                     | `[]`                 | Pas de croissance, chaque valeur isolée est une série (on garde `[2]` car la fonction prend la dernière série équivalente) |
| Croissance continue                  | `[1, 2, 3, 4, 5]`             | `[1, 2, 3, 4, 5]`    | Toute la liste est une série croissante                                                                                    |
| Plusieurs séries                     | `[5, 6, 2, 3, 4, 1]`          | `[2, 3, 4]`          | Deux séries `[5, 6]` et `[2, 3, 4]`, la plus longue est `[2, 3, 4]`                                                        |
| Série en fin de liste                | `[7, 1, 2, 3, 4]`             | `[1, 2, 3, 4]`       | La série la plus longue est à la fin                                                                                       |
| Série au début                       | `[1, 2, 3, 0, 5]`             | `[1, 2, 3]`          | La plus longue série croissante est en début de liste                                                                      |
| Valeurs identiques                   | `[3, 3, 3, 3]`                | `[]`                 | Pas de croissance (égalité ne compte pas), chaque valeur forme une série de longueur 1                                     |
| Cas mixte avec longue série finale   | `[2, 5, 1, 2, 3, 4, 0]`       | `[1, 2, 3, 4]`       | Plusieurs séries mais la plus longue est au milieu-fin                                                                     |
| Listes avec nombres négatifs         | `[5, -3, -1, -2, 0]`          | `[]`                 | La fonction doit afficher un message d'erreur.                                                                             |
| Liste avec doublons                  | `[1, 2, 2, 3, 4]`             | `[2, 3, 4]`          | Les doublons interrompent la croissance, la série commence après le doublon                                                |

# Tableau de tests – Fonction `moyennes_ventes_par_periode`
| Cas de test                                   | Entrée `ventes`                        | Entrée `periode`   | Résultat attendu                               | Remarques                                                  |
|-----------------------------------------------|----------------------------------------|--------------------|------------------------------------------------|------------------------------------------------------------|
| Ventes parfaitement divisibles en périodes    | `[10, 20, 30, 40]`                     | `2`                | `[15.0, 35.0]`                                 |                                                            |
| Ventes non parfaitement divisibles            | `[10, 20, 30, 40, 50]`                 | `2`                | `[15.0, 35.0]`                                 | La dernière valeur (50) est ignorée car période incomplète |
| Période = 1                                   | `[5, 15, 25]`                          | `1`                | `[5.0, 15.0, 25.0]`                            | Chaque valeur devient sa propre moyenne                    |
| Période = taille exacte de la liste           | `[10, 20, 30]`                         | `3`                | `[20.0]`                                       | Moyenne unique sur toute la liste                          |
| Longue liste avec période 3                   | `[10, 20, 30, 40, 50, 60, 70, 80, 90]` | `3`                | `[20.0, 50.0, 80.0]`                           |                                                            |
| Valeurs négatives                             | `[10, -5, 15, -5]`                     | `2`                | `[]`                                           | "Impossible d'avoir des ventes négatives!"                 |
|                                               |                                        |                    |                                                |                                                            |
| Cas limite                                    |                                        |                    |                                                |                                                            |
| Période = 0                                   | `[10, 20, 30]`                         | `0`                | `[]` avec message d'erreur (division par zéro) | Cas extrême à gérer avec une validation ou un try/except   |
| Période négative                              | `[10, 20, 30]`                         | `-2`               | `[]` avec message d'erreur                     | Validation                                                 |
| Liste vide                                    | `[]`                                   | `3`                | `[]`                                           | Pas de ventes, résultat vide                               |
| Une seule valeur, période 1                   | `[10]`                                 | `1`                | `[10]`                                         |                                                            |
| Période plus grande que la taille de la liste | `[5, 10]`                              | `5`                | `[]`                                           | Aucune période complète atteinte                           |

# Tableau de tests – Fonction `meilleure_periode`
| Cas de test                        | Entrée `moyennes_ventes` | Résultat attendu | Remarques / explication                                    |
|------------------------------------|--------------------------|------------------|------------------------------------------------------------|
| Liste vide                         | `[]`                     | `None`           | Pas de données, retourne `None`                            |
| Une seule valeur                   | `[50]`                   | `1`              | Une seule période, donc la première                        |
| Valeurs identiques                 | `[20, 20, 20, 20]`       | `1`              | Max = 20, premier indice --> période 1                     |
| Valeurs mixtes                     | `[15, 25, 10, 30, 5]`    | `4`              | Max = 30 à l’indice 3 --> période 4                        |
| Longue liste avec plusieurs maxima | `[5, 100, 50, 100, 20]`  | `2`              | Plusieurs 100, prend le premier à l’indice 1 --> période 2 |
