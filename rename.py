import os
import time


time.sleep(10)
files = os.listdir(path = "F:\Movie\The-Mentalist")

for file in files:
    withdot = 0
    newname = ""
    for letter in file:
        if letter == "_":
            withdot = 1
            newname = newname + "."
        else:
            newname = newname + letter
    if withdot == 1:
        os.rename(f"F:\Movie\The-Mentalist\{file}", f"F:\Movie\The-Mentalist\{newname}")