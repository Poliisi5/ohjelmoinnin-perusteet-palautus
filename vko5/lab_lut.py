#!/usr/bin/env python3
"""Validation module for the LAB programming basics, week 5 task 3."""


import random


# ------------------------- ALOITA TEHTÄVÄN TOTEUTUS TÄSTÄ ---------------------------- #

def lab_lut(n, a, b):
    if n % a == 0 and n % b == 0:
        return "lablut"
    elif n % a == 0:
        return "lab"
    elif n % b == 0:
        return "lut"
    else:
        return f"{n:d}"


def lab_lut_plus(n, a, b):
        """."""
        if n % a == 0 and n % b == 0 and a > b:
            return "lablut"
        elif n % a == 0 and n % b == 0 and b > a:
            return "lutlab"
        elif n % a == 0 and n % b == 0 and a == b:
            return "lablutlab"
        elif n % a == 0:
            return "lab"
        elif n % b == 0:
            return "lut"
        else:
            return f"{n:d}"


















































# ----------------------- TEHTÄVÄN TOTEUTUS ENNEN TÄTÄ RIVIÄ -------------------------- #

# Tarkistuskoodi alkaa

def validate_lab_lut():
    """Verify that the function lab_lut works as intended."""
    def mock_lab_lut(n, a, b):
        """."""
        if n % a == 0 and n % b == 0:
            return "lablut"
        elif n % a == 0:
            return "lab"
        elif n % b == 0:
            return "lut"
        else:
            return f"{n:d}"

    # Tarkistetaan funktion suoritus satunnaisilla arvoilla
    try:
        for _ in range(0, 100):
            div_1 = random.randint(2, 20)
            div_2 = random.randint(2, 20)

            for i in range(1, 10000):
                v = lab_lut(i, div_1, div_2)
                if v != mock_lab_lut(i, div_1, div_2):
                    print("Funktio lab_lut on toteutettu väärin.")
                    print(f"Arvo {i}, jakaja 1 {div_1}, jakaja 2 {div_2}")
                    print(f"Saatiin {v}, oikea vastaus {mock_lab_lut(i, div_1, div_2)}")
                    return False
    except NameError:
        print("Funktio lab_lut ei ole vielä määritelty.")
        return False

    print("Funktio lab_lut on toteutettu oikein.")
    return True


def validate_lab_lut_plus():
    """Verify that the function lab_lut_plus works as intended."""
    def mock_lab_lut_plus(n, a, b):
        """."""
        if n % a == 0 and n % b == 0 and a > b:
            return "lablut"
        elif n % a == 0 and n % b == 0 and b > a:
            return "lutlab"
        elif n % a == 0 and n % b == 0 and a == b:
            return "lablutlab"
        elif n % a == 0:
            return "lab"
        elif n % b == 0:
            return "lut"
        else:
            return f"{n:d}"

    # Tarkistetaan funktion suoritus satunnaisilla arvoilla
    try:
        for _ in range(0, 100):
            div_1 = random.randint(2, 20)
            div_2 = random.randint(2, 20)

            for i in range(1, 10000):
                v = lab_lut_plus(i, div_1, div_2)
                if v != mock_lab_lut_plus(i, div_1, div_2):
                    print("Funktio lab_lut on toteutettu väärin.")
                    print(f"Arvo {i}, jakaja 1 {div_1}, jakaja 2 {div_2}")
                    print(f"Saatiin {v}, oikea vastaus {mock_lab_lut_plus(i, div_1, div_2)}")
                    return False

        # Varmistetaan, että reunatapaus jakaja 1 == jakaja 2 tulee tarkistettua
        div_1 = random.randint(2, 20)
        div_2 = div_1
        for i in range(1, 10000):
            v = lab_lut_plus(i, div_1, div_2)
            if v != mock_lab_lut_plus(i, div_1, div_2):
                print("Funktio lab_lut on toteutettu väärin.")
                print(f"Arvo {i}, jakaja 1 {div_1}, jakaja 2 {div_2}")
                print(f"Saatiin {v}, oikea vastaus {mock_lab_lut_plus(i, div_1, div_2)}")
                return False
    except NameError:
        print("Funktio lab_lut_plus ei ole vielä määritelty.")
        return False

    print("Funktio lab_lut_plus on toteutettu oikein.")
    return True


def main():
    """Verify all functions."""
    answers = [
        validate_lab_lut(),
        validate_lab_lut_plus(),
    ]

    if False in answers:
        print("Osa kohdista on vielä väärin, jatka yrittämistä.")
        return False

    print("Kaikki kohdat ovat oikein, onneksi olkoon!")
    return True


if __name__ == "__main__":
    main()
