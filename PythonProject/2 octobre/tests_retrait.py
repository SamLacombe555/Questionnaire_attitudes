from SolutionDebug2 import retrait  # adapte au vrai nom de ton fichier


def test_retrait_normal():
    # Arrange
    solde = 1000
    montant = 200

    # Act
    result = retrait(solde, montant)

    # Assert
    assert result == 800


def test_retrait_negatif():
    # Arrange
    solde = 1000
    montant = -50

    # Act
    result = retrait(solde, montant)

    # Assert
    assert result == 1000


def test_retrait_superieur_solde():
    # Arrange
    solde = 1000
    montant = 1200

    # Act
    result = retrait(solde, montant)

    # Assert
    assert result == 0


def test_retrait_nul():
    # Arrange
    solde = 1000
    montant = 0

    # Act
    result = retrait(solde, montant)

    # Assert
    assert result == 1000


def test_retrait_exact():
    # Arrange
    solde = 500
    montant = 500

    # Act
    result = retrait(solde, montant)

    # Assert
    assert result == 0
