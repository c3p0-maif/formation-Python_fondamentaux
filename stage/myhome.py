"""
Module de contrôle du confort à la maison… Ou plutôt, qui va le simuler.
"""

T_MAX = 26
T_MIN = 18


def get_comfort(temperature):
    if int(temperature) > T_MAX:
        return "Il fait trop chaud"
    elif int(temperature) < T_MIN:
        return "Il fait trop froid"
    return "Tout va bien"


def get_comfort_2(temperature):
    return "il fait bon" if T_MIN < int(temperature) < T_MAX else "il ne fait pas bon"
