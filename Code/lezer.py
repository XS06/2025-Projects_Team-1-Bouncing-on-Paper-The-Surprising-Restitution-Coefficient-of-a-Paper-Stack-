# Naam: Saladin Shah
# Studentnummer: 15817490


import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv


with open('1-2-M.csv', 'r') as yurr:
    hoogte_lijst = []
    tijd_lijst = []
    teller = 0
        
    for regel in yurr:
        data_opgeknipt = regel.strip().split()

        if teller == 3:
            print('daggoe')
        else:    
            if data_opgeknipt and data_opgeknipt[0] != 'Frame':
                if data_opgeknipt and data_opgeknipt[0] != 'Tracks':
                    if data_opgeknipt and data_opgeknipt[0] != 'Track':
                        tijd = int(data_opgeknipt[0])
                        y1 = float(data_opgeknipt[2])
                        hoogte = 1000 - y1

                        tijd_lijst.append(tijd)
                        hoogte_lijst.append(hoogte)
                    else:
                        teller +=1
                else:
                    teller +=1
            else:
                teller +=1
    print(hoogte_lijst)
    print(tijd_lijst)


plt.plot(tijd_lijst, hoogte_lijst)
plt.xlabel('Frame (geen eenheid)')
plt.ylabel('Hoogte (px)')
plt.show()