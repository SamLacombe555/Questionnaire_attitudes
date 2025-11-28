import pytest
import jeu_cartes_solution as jeu

def test_generer_paquet_carte():
    # Arrange
    valeurs_cartes = ["As", "2", "3", "Reine"]
    suites_cartes = ["Pique", "Coeur"]

    resultat_attendu = ['As de Pique', '2 de Pique', '3 de Pique', 'Reine de Pique',
                        'As de Coeur', '2 de Coeur', '3 de Coeur', 'Reine de Coeur']

    # Act
    resultat_observe = jeu.generer_paquet_carte(suites=suites_cartes, valeurs=valeurs_cartes)

    # Assert
    #assert resultat_observe == resultat_attendu
    for carte in resultat_observe:
        assert carte in resultat_attendu

    assert len(resultat_observe) == len(resultat_attendu)

def test_definir_carte_a_piger():
    # Arrange
    paquet = ['As de Pique', '2 de Pique', '3 de Pique', 'Reine de Pique', 'As de Coeur']

    # Act
    resultat_observe_carte_pigee = jeu.definir_carte_a_piger(paquet)

    # Assert
    assert resultat_observe_carte_pigee in paquet

def test_simuler_partie_cartes():
    """
    Pour la fonction simuler_partie_cartes,
    on ne vérifie que si le le nombre de paramètres est bon.
    """

    # Arrange:
    nb_parametres_attendu = 2

    # Act: Récupération du nombre de paramètres de la fonction
    nb_parametres_obtenu = jeu.simuler_partie_cartes.__code__.co_argcount

    # Assert:
    assert nb_parametres_obtenu == nb_parametres_attendu, (f"Indice : le nombre de paramètres doit être {nb_parametres_attendu}, "
                                                           f"mais {nb_parametres_obtenu} ont été fournis.")
