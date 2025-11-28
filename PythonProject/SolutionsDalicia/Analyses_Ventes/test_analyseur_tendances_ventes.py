import pytest
from analyseur_tendances_ventes import trouver_plus_longue_serie_croissante, moyennes_ventes_par_periode, meilleure_periode

"""
Tests unitaires de la fonction trouver_plus_longue_serie_croissante
"""
@pytest.mark.parametrize(
    "ventes,                    attendu", [
    ([],                          []),               # Liste vide
    ([5],                         []),               # Un seul élément
    ([3, 7],                      [3, 7]),           # Deux valeurs croissantes
    ([10, 2],                     []),               # Deux valeurs décroissantes
    ([1, 2, 3, 4, 5],             [1, 2, 3, 4, 5]),  # Croissance continue
    ([5, 6, 2, 3, 4, 1],          [2, 3, 4]),        # Plusieurs séries
    ([7, 1, 2, 3, 4],             [1, 2, 3, 4]),     # Série en fin de liste
    ([1, 2, 3, 0, 5],             [1, 2, 3]),        # Série au début
    ([3, 3, 3, 3],                []),               # Valeurs identiques
    ([2, 5, 1, 2, 3, 4, 0],       [1, 2, 3, 4]),     # Cas mixte avec longue série finale
    ([5, -3, -1, -2, 0],          []),               # Listes avec nombres négatifs
    ([1, 2, 2, 3, 4],             [2, 3, 4]),        # Liste avec doublons
])
def test_trouver_plus_longue_serie_croissante(ventes, attendu):
    assert trouver_plus_longue_serie_croissante(ventes) == attendu

"""
Tests unitaires de la fonction moyennes_ventes_par_periode
"""
@pytest.mark.parametrize(
    "ventes,                                periode, attendu",
    [([10, 20, 30, 40],                     2,      [15.0, 35.0]),      # Ventes_version1 parfaitement divisibles
     ([10, 20, 30, 40, 50],                 2,      [15.0, 35.0]),      # Ventes_version1 non parfaitement divisibles
     ([5, 15, 25],                          1,      [5.0, 15.0, 25.0]), # Période = 1
     ([10, 20, 30],                         3,      [20.0]),            # Période = taille exacte de la liste
     ([10, 20, 30, 40, 50, 60, 70, 80, 90], 3,      [20.0, 50.0, 80.0]),# Longue liste avec période 3
     ([10, -5, 15, -5],                     2,      []),                # Valeurs négatives
     ([10, 20, 30],                         0,      []),                # Période = 0
     ([10, 20, 30],                         -2,     []),                # Période négative
     ([],                                   3,      []),                # Liste vide
     ([10],                                 1,      [10]),              # Une seule valeur, période 1
     ([5, 10],                              5,      []),                # Période plus grande que la taille
    ])
def test_moyennes_ventes_par_periode(ventes, periode, attendu):
    # Act
    resultat = moyennes_ventes_par_periode(ventes, periode)

    # Assert
    assert resultat == attendu


"""
Tests unitaires de la fonction meilleure_periode
"""
@pytest.mark.parametrize(
    "moyennes_ventes, attendu",
    [
        ([], None),                      # Liste vide
        ([50], 1),                       # Une seule valeur
        ([20, 20, 20, 20], 1),           # Valeurs identiques
        ([15, 25, 10, 30, 5], 4),        # Valeurs mixtes
        ([5, 100, 50, 100, 20], 2),      # Longue liste avec plusieurs maxima
    ]
)
def test_meilleure_periode(moyennes_ventes, attendu):
    # Act
    resultat = meilleure_periode(moyennes_ventes)

    # Assert
    assert resultat == attendu
