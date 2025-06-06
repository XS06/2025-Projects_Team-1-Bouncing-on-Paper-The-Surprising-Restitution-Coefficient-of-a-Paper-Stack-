# Naam: Saladin Shah
# Studentnummer: 15817490


import numpy as np
import math as mt
import matplotlib.pyplot as plt
import random as rand


with open('1-1-M.csv', 'r') as yurr:
    hoogte_lijst = []
    tijd_lijst = []
    teller = 0

    while teller < 3:
        
        for regel in yurr:
            data_opgeknipt = regel.split('  ')

            if data_opgeknipt[0] == str:
                tijd = int(data_opgeknipt[0])
                hoogte = float(data_opgeknipt[2])

                tijd_lijst.append(tijd)
                hoogte_lijst.append(hoogte)
                teller +=1

plt.plot(tijd_lijst, hoogte_lijst)
plt.xlabel('Frame (geen eenheid)')
plt.ylabel('Hoogte (px)')
plt.show()