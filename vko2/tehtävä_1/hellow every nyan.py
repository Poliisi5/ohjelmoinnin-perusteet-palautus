import time
import random
string = ["H","e","ll","ow"," ","Ev","e","ry"," ","Ny","an"]
for i in string:
    print(f"{i}", end="", flush=True)
    time.sleep(random.randrange(5))