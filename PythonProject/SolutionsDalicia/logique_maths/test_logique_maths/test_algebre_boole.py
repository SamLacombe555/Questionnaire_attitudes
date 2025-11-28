import pytest
from Semaine11.logique_maths.app_logique_maths import algebre_boole_solution

@pytest.mark.parametrize("proposition, resultat_attendu",[
    ("|p + q", True),
    ("(p.q)+|(p+q)", True),
    ("r + |p", False),
    ("p", True)
])
def test_proposition_valide(proposition, resultat_attendu):
    # Arrange

    #Act
    resultat_obtenu = algebre_boole_solution.proposition_valide(proposition)

    # Assert
    assert resultat_obtenu == resultat_attendu
