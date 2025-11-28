import pytest
from fctListes import *

@pytest.mark.parametrize(
    "vie, defense, attaque, attendu",
    [
        (100, 10, 30, 80),    # attaque > defense
        (50, 20, 20, 50),     # attaque = defense
        (70, 40, 10, 70),     # attaque < defense
        (10, 0, 50, 0),       # vie ne peut pas être négative
        (1, 0, 5, 0),         # vie faible
    ]
)
def test_points_de_vie_restants(vie, defense, attaque, attendu):
    assert points_de_vie_restants(vie, defense, attaque) == attendu


@pytest.mark.parametrize(
    "legos, couleur, attendu",
    [
        (["rouge", "bleu", "rouge"], "rouge", 66.6666666667),
        (["vert", "bleu", "rouge"], "bleu", 33.3333333333),
        (["rouge", "bleu"], "vert", 0.0),
        ([], "rouge", 0.0),
        (["jaune", "jaune"], "jaune", 100.0),
    ]
)
def test_pourcentage_couleur(legos, couleur, attendu):
    resultat = pourcentage_couleur(legos, couleur)
    assert pytest.approx(resultat, rel=1e-2) == attendu


@pytest.mark.parametrize(
    "legos, attendu",
    [
        (["rouge", "bleu", "bleu", "rouge"], 2.0),
        (["jaune", "jaune", "jaune"], 3.0),
        (["rouge"], 1.0),
        ([], 0.0),
    ]
)
def test_moyenne_blocs_par_couleur(legos, attendu):
    assert moyenne_blocs_par_couleur(legos) == attendu
