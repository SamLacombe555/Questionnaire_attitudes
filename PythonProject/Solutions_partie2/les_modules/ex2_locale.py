from datetime import date
import locale

locale.setlocale(locale.LC_ALL, "fr_CA.utf8")

def afficher_date_complete(annee, mois, jour):
    """Transforme et affiche la date dans le bon format."""
    d = date(annee, mois, jour)
    print(d.strftime("%A %d %B %Y"))

# Exemple d'utilisation
annee = int(input("Entrez une année : "))
mois = int(input("Entrez un mois (1-12) : "))
jour = int(input("Entrez un jour (1-31) : "))

afficher_date_complete(annee, mois, jour)
