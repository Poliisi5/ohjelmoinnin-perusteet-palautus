#!/usr/bin/env python3
"""Validation module for the LAB programming basics, week 5 task 1."""
import random

# ------------------------- ALOITA TEHTÄVÄN TOTEUTUS TÄSTÄ ---------------------------- #

def sum_values(sum_1, sum_2 ):
    return(sum_1 + sum_2)

def sub_values(sub_1, sub_2):
    return(sub_1 - sub_2)

def mul_values(mul_1, mul_2):
    return(mul_1 * mul_2)

def div_values(div_1, div_2):
    if div_2 == 0:
        return
    else:
        return(div_1 / div_2)
        

























































# ----------------------- TEHTÄVÄN TOTEUTUS ENNEN TÄTÄ RIVIÄ -------------------------- #

# Tarkistuskoodi alkaa
def validate_sum_values():
    """Verify the answer provided by sum_values is correct."""
    try:
        # Tarkista funktio kymmenen kertaa satunnaisilla arvoilla
        for _ in range(0, 10):
            x = random.randint(0, 10000)
            y = random.randint(0, 10000)
            v = sum_values(x, y)
            if v != x + y:
                print("Funktio sum_values on toteutettu väärin.")
                print(f"Haluttu arvo f{x + y}, saatiin arvo {v}.")
                return False

        print("Funktio sum_values on toteutettu oikein.")
    except NameError:
        print("Funktio sum_values ei ole vielä määritelty.")
        return False

    return True

def validate_sub_values():
    """Verify the answer provided by sub_values is correct."""
    try:
        # Tarkista funktio kymmenen kertaa satunnaisilla arvoilla
        for _ in range(0, 10):
            x = random.randint(0, 10000)
            y = random.randint(0, 10000)
            v = sub_values(x, y)
            if v != x - y:
                print("Funktio sub_values on toteutettu väärin.")
                print(f"Haluttu arvo f{x - y}, saatiin arvo {v}.")
                return False

        print("Funktio sub_values on toteutettu oikein.")
    except NameError:
        print("Funktio sub_values ei ole vielä määritelty.")
        return False

    return True

def validate_mul_values():
    """Verify the answer provided by mul_values is correct."""
    try:
        # Tarkista funktio kymmenen kertaa satunnaisilla arvoilla
        for _ in range(0, 10):
            x = random.randint(0, 10000)
            y = random.randint(0, 10000)
            v = mul_values(x, y)
            if v != x * y:
                print("Funktio mul_values on toteutettu väärin.")
                print(f"Haluttu arvo f{x * y}, saatiin arvo {v}.")
                return False

        print("Funktio mul_values on toteutettu oikein.")
    except NameError:
        print("Funktio mul_values ei ole vielä määritelty.")
        return False

    return True

def validate_div_values():
    """Verify the answer provided by div_values is correct."""
    try:
        # Tarkista funktio kymmenen kertaa satunnaisilla arvoilla
        for _ in range(0, 10):
            x = random.randint(0, 10000)
            y = random.randint(1, 10000)
            v = div_values(x, y)
            if v != x / y:
                print("Funktio div_values on toteutettu väärin.")
                print(f"Haluttu arvo f{x / y}, saatiin arvo {v}.")
                return False

        # Tarkista nollalla jakamisen reunatapaus
        try:
            v = div_values(10, 0)
            if v is not None:
                print("Funktio div_values on toteutettu väärin.")
                print("Funktio palauttaa arvon jaetttaessa nollalla.")
                return False
        except ZeroDivisionError:
            print("Funktio div_values ei estä nollalla jakamista.")
            return False

        print("Funktio div_values on toteutettu oikein")
    except NameError:
        print("Funktio div_values ei ole vielä määritelty.")
        return False

    return True


def main():
    """Verify all the functions."""
    answers = [
        validate_sum_values(),
        validate_sub_values(),
        validate_mul_values(),
        validate_div_values(),
    ]

    if False in answers:
        print("Osa kohdista on vielä väärin, jatka yrittämistä.")
        return False

    print("Kaikki kohdat ovat oikein, onneksi olkoon!")
    return True


if __name__ == "__main__":
    main()
