import pytest
from SolutionDebug3 import roche_papier_ciseau

# Arrange
@pytest.mark.parametrize("j1, j2, resultat_attendu",[
    ("roche", "ciseau", "joueur 1 gagne avec roche"),
    ("roche", "papier", "joueur 2 gagne avec papier"),
    ("Roche", "Papier", "joueur 2 gagne avec papier"),
    ("allo", "", None)
])
def test_rpc(j1, j2, resultat_attendu):
    # Act
    resultat = roche_papier_ciseau(j1, j2)
    # Assert
    assert resultat == resultat_attendu


@pytest.mark.parametrize("a, b, resultat_attendu", [
    (10, 2, 5),
    (-10, 2, -5),
    (3, 2, 1),
    (1000000, 10, 100000),
    (0, 5, 0),
    (1, 3, 0)
])
def test_division_entiere(a, b, resultat_attendu):
    # Arrange
    # Act
    resultat = demo.division_entiere(a, b)

    # Assert
    assert isinstance(resultat, int)
    assert resultat == resultat_attendu


# Ici, l'exception ZeroDivisionError est gérée, ce teste va donc passer.
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_exception_zero_division_entiere():
    resultat = demo.division_entiere(5, 0)
    resultat_attendu = 999999999
    assert resultat == resultat_attendu


# Ici, l'exception TypeError n'est pas gérée, ce teste NE va donc PAS passer.
@pytest.mark.xfail(raises=TypeError)
def test_exception_TypeError_division_entiere():
    resultat = demo.division_entiere("10", "5")
    resultat_attendu = None
    assert resultat == resultat_attendu
"""