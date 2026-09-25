#!/usr/bin/env python3


# Tehtävän alustus (initialization) ja kirjastojen tuonti
import random

luku: int = random.randint(0, 100000)
vastaus: str = ""


# ------------------------- ALOITA TEHTÄVÄN TOTEUTUS TÄSTÄ ---------------------------- #

print(f"{range(2, int(luku / 2 + 1))}")

if luku > 0: 
    for test in range(2, int(luku / 2 + 1)):
        if luku % test == 0:
            vastaus = f"{luku} ei ole alkuluku, jaollinen {test}:lla"
else:
    vastaus = "luku on 0"
if not vastaus:
    vastaus = f"{luku} on alkuluku"















































# ----------------------- TEHTÄVÄN TOTEUTUS ENNEN TÄTÄ RIVIÄ -------------------------- #

# Tarkistuskoodi alkaa
oikea_vastaus = ""

if luku > 0:
    for i in range(2, int(luku / 2 + 1)):
        if luku % i == 0:
            oikea_vastaus = f"{luku} ei ole alkuluku, jaollinen {i}:lla"
else:
    oikea_vastaus = "luku on 0"
if not oikea_vastaus:
    oikea_vastaus = f"{luku} on alkuluku"

if vastaus == oikea_vastaus:
    print(f"Vastaus on oikein. Saatiin vastaus: {vastaus}")
else:
    print(f"""Vastaus on väärin.
Annettu vastaus: {vastaus}
Oikea vastaus: {oikea_vastaus}""")
