history = []

def main():
    quit = False
    print("Laskin käynnistyy...")
    print_help()
    while quit == False:
        current = input("> ")
        if " " in current:
            current_processed = current.split(" ")
            if current_processed[1] == "+":
                sum(current_processed[0],current_processed[2])
            elif current_processed[1] == "-":
                minus(current_processed[0],current_processed[2])
            elif current_processed[1] == "*":
                mult(current_processed[0],current_processed[2])
            elif current_processed[1] == "/":
                div(current_processed[0],current_processed[2])
            else:
                print(f"Tuntematon komento {current}. Voit tulostaa apuviestin komennolla ? tai h.")
        elif current == "p":
            print_history()
        elif current == "h" or current == "?":
            print_help()
        elif current == "q":
            quit = True
        #elif :
        #    print("Numbers and operators must be divided by a space")
        else:
            print(f"Tuntematon komento {current}. Voit tulostaa apuviestin komennolla ? tai h.")


    print("Lopetetaan ohjelma...")

def check_number(a):
    try:
        float(a)
        return True
    except (ValueError, TypeError):
        return False

def print_help():
    print("""Ohjelmassa on saatavilla seuraavat toiminnot:
    +   – laske numeroiden summa
    -   – laske numeroiden erotus
    *   – laske numeroiden tulo
    /   – laske numeroiden osamäärä
    p   – tulosta operaatioiden historia
    q   – lopeta ohjelma (myös tyhjä syöte lopettaa ohjelman)
    ?,h – tulosta tämä viesti""")

def save_history(a):
    history.append(a)
    while len(history) >= 10:
        history.pop(0)

def print_history():
    counter = 0
    while len(history) != counter:
        print(history[counter])
        counter = counter + 1   

def sum(a, b):
    if check_number(a) == False or check_number(b) == False:
        print(f"""Syötteen muuttaminen numeroiksi epäonnistui. Syötettiin arvot {a} ja {b}.
Syötä vain kokonais- tai desimaalilukuja.""")
    else:
        c = f"{a} + {b} = {int(a)+int(b)}"
        print(c)
        save_history(c)

def minus(a, b):
    if check_number(a) == False or check_number(b) == False:
        print(f"""Syötteen muuttaminen numeroiksi epäonnistui. Syötettiin arvot {a} ja {b}.
Syötä vain kokonais- tai desimaalilukuja.""")
    else:
        c = f"{a} - {b} = {int(a)-int(b)}"
        print(c)
        save_history(c)

def mult(a, b):
    if check_number(a) == False or check_number(b) == False:
        print(f"""Syötteen muuttaminen numeroiksi epäonnistui. Syötettiin arvot {a} ja {b}.
Syötä vain kokonais- tai desimaalilukuja.""")
    else:
        c = f"{a} * {b} = {int(a)*int(b)}"
        print(c)
        save_history(c)

def div(a, b):
    if check_number(a) == False or check_number(b) == False:
        print(f"""Syötteen muuttaminen numeroiksi epäonnistui. Syötettiin arvot {a} ja {b}.
Syötä vain kokonais- tai desimaalilukuja.""")
    elif b == 0:
        print("Cannot Divide by zero")
    else:
        c = f"{a} / {b} = {int(a)/int(b)}"
        print(c)
        save_history(c)
    
    

main()