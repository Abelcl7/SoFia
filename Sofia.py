#Evil SoFiA 
import re
import time 
from random import choice
import os
import sys
import json

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


vrs = ('mOS VERSION - 04920\n')
time.sleep(0.5)

try:
    import requests
except:
    print(" Installing requests Module")
    if os.name=='nt':
        try:
            os.system('C:\Python27\Scripts\pip2.exe install requests')
        except:
            print ("Install Python-Pip Sir")
            raw_input('')
    else:
        os.system('pip2 install requests')
msg001 = ("""
                                     _       
                                    | |      
  ___ __ _ _ __ __ _  __ _ _ __   __| | ___  
 / __/ _` | '__/ _` |/ _` | '_ \ / _` |/ _ \ 
| (_| (_| | | | (_| | (_| | | | | (_| | (_) |
 \___\__,_|_|  \__, |\__,_|_| |_|\__,_|\___/ 
                __/ |                        
               |___/                         
""")

print(msg001)
msg00 = "OOO\n"
for i in msg00:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.2)

ax = os.system
cls()

ols = time.strftime("%H:%M:%S")
print time.strftime("                    %I:%M:%S") 
if ols > "23:30":
    print ("EVIL SOFIA ESTA REFRESCANDO!...")
    print("CODIFICADO EN: ")
    print ('''
                _
        ,--(_)         @               @
      _/ ;-. \    @  @ @,m. @  @ ,mm. m@m  @  @
     (_)(   )-)   @  @ @  8 @  @ @  @  @   @  @
       \ ;-'_/    `""' `""' `""' "  "  `"" `""'
 -BOG-  `--(_)
''')

    exit()
else:
    print (" ")


print("    ___ _   _  _ _      __   __  ___ _  __   ")
print("   | __| \ / || | |   /' _/ /__\| __| |/  \  ")
print("   | _|`\ V /'| | |_  `._`.| \/ | _|| | /\ | ")
print("   |___| \_/  |_|___| |___/ \__/|_| |_|_||_|  ")

time.sleep(1.4)

print ("		Abel Coloch 		")
print ("		~SoFia~			")
print ('''

''')

while True:
    print("      .:MENU:.")
    print("   1.EXTRAPOLADOR")
    print("")
    opc = input("  Digite el numero de la opcion: ")


    if opc == 1:
        Bin = int(input("Digite los primeros 8 digitos del Bin: "))
        lista = []
        Intro = lista.append(Bin)

        #Primer Bin
        bin11 = int(input("Digito 10 BIN UNO: "))
        if bin11 >= 0 and bin11 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin11 = int(input("Vuelve a introducir el digito: "))

        bin12 = int(input("Digito 11 BIN UNO: "))
        if bin12 >= 0 and bin12 <= 9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin12 = int(input("Introduce el digito numero ONCE del primer Bin: "))

        #Segundo Bin

        bin21 = int(input("Digito 10 BIN DOS: "))
        if bin21 >= 0 and bin21 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin21 = int(input("Vuelve a introducir el digito: "))

        bin22 = int(input("Digito 11 BIN DOS: "))
        if bin22 >= 0 and bin22 <=9:
            print("")
        else:
            print("Introduce un numero correcto :)")
            bin22 = int(input("Introduce el digiro numero ONCE del segundo Bin: "))

        #Algoritmo

        A = (bin11 + bin21 / 2) * 5
        B = (bin12 + bin22 / 2) * 5
        C = A + B

        #Agregar los digitos

        Intro2 = lista.append(C)
        print("Tu extrapolacion es: ")
        time.sleep(0.8)
        print("".join(repr(e) for e in lista))
        print("")
        time.sleep(2)
