from datetime import date

def jours_avant(date_future):
    """Affiche dans combien de jours la date future arrivera."""
    aujourd_hui = date.today()
    difference = date_future - aujourd_hui
    print(f"Il reste {difference.days} jours avant le {date_future}")

# Exemple : date future choisie
date_future = date(2026, 1, 1)
jours_avant(date_future)
