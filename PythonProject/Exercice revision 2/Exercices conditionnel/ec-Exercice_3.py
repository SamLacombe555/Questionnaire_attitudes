"""
================================================
RAPPORT DE MISSION : ALGONOVA
Nom mission : -----------AlgoNova-----------
Nombres d'astronautes : 6 (masse totale 480 kg)
Modules disponibles : 3 (masse totale 1500 kg)
Masse totale du vaisseau : 1980 kg
Carburant nécessaire : 3960.00 litres
Mission VIP, bonus VIP applicable.
	Carburant après bonus VIP : 4010.00 litres
Mission réalisable (carburant suffisant)
Départ autorisé uniquement car mission VIP
=================================================
================================================
RAPPORT DE MISSION : ALGONOVA
Nom mission : -----------AlgoNova-----------
Nombres d'astronautes : 6 (masse totale 480 kg)
Modules disponibles : 3 (masse totale 1500 kg)
Masse totale du vaisseau : 1980 kg
Carburant nécessaire : 3960.00 litres
Mission réalisable (carburant suffisant)
Départ interdit (tempête solaire)
=================================================
"""

def masse_astronautes(nbr_astro) -> float:
    return nbr_astro*80

def carburant(masse_vaisseau):
    return masse_vaisseau*2
