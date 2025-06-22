# Naam: Saladin Shah
# Studentnummer: 15817490


import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv
import statistics as stat


A4_CSV = open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4_sanitized_data.csv', 'r')
A5_B_CSV = open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5_B_sanitized_data.csv', 'r')
A5_O_CSV = open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5_O_sanitized_data.csv', 'r')

# A4_CSV = open('C:/Users/salad/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4_sanitized_data.csv', 'r')
# A5_B_CSV = open('C:/Users/salad/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5_B_sanitized_data.csv', 'r')
# A5_O_CSV = open('C:/Users/salad/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5_O_sanitized_data.csv', 'r')


with A4_CSV as A4:
    A4_papier_lijst = []
    A4_coefficienten_1_h_lijst = []
    A4_fout_coefficienten_1_h_lijst = []
    A4_coefficienten_1_v_lijst = []
    A4_fout_coefficienten_1_v_lijst = []

    A4_compressed_papier_lijst = []
    A4_avg_h_lijst = []
    A4_fout_h_lijst = []
    A4_avg_v_lijst = []
    A4_fout_v_lijst = []

    for row in A4:
        column = row.split(',')

        if column[0] != 'A4_papier_lijst':
            A4_papier_lijst.append(int(column[0]))
            A4_coefficienten_1_h_lijst.append(np.sqrt(float(column[1])))
            A4_fout_coefficienten_1_h_lijst.append(float(column[2]))
            A4_coefficienten_1_v_lijst.append(float(column[3]))
            A4_fout_coefficienten_1_v_lijst.append(float(column[4]))
    
    for papier in range(0, int(len(A4_papier_lijst) - 2)):
        if A4_papier_lijst[papier] == A4_papier_lijst[papier + 1] == A4_papier_lijst[papier + 2]:
            A4_compressed_papier_lijst.append(A4_papier_lijst[papier])
            A4_temp_h_list = [A4_coefficienten_1_h_lijst[papier], A4_coefficienten_1_h_lijst[papier + 1], A4_coefficienten_1_h_lijst[papier + 2]]
            A4_fout_temp_h_list = [A4_fout_coefficienten_1_h_lijst[papier], A4_fout_coefficienten_1_h_lijst[papier + 1], A4_fout_coefficienten_1_h_lijst[papier + 2]]
            A4_avg_h_lijst.append(float(np.mean(A4_temp_h_list)))
            A4_fout_h_lijst.append(float(np.sqrt(np.std(A4_temp_h_list) + np.var(A4_fout_temp_h_list))))
            A4_temp_v_list = [A4_coefficienten_1_v_lijst[papier], A4_coefficienten_1_v_lijst[papier + 1], A4_coefficienten_1_v_lijst[papier + 2]]
            A4_fout_temp_v_list = [A4_fout_coefficienten_1_v_lijst[papier], A4_fout_coefficienten_1_v_lijst[papier + 1], A4_fout_coefficienten_1_v_lijst[papier + 2]]
            A4_avg_v_lijst.append(float(np.mean(A4_temp_v_list)))
            A4_fout_v_lijst.append(float(np.sqrt(np.std(A4_temp_v_list) + np.var(A4_fout_temp_v_list))))
        

    A4_CSV.close()


with A5_B_CSV as A5_B:
    A5_papier_lijst = []
    A5_coefficienten_1_h_B_lijst = []
    A5_fout_coefficienten_1_h_B_lijst = []
    A5_coefficienten_1_v_B_lijst = []
    A5_fout_coefficienten_1_v_B_lijst = []

    A5_compressed_papier_lijst = []
    A5_avg_h_B_lijst = []
    A5_fout_h_B_lijst = []
    A5_avg_v_B_lijst = []
    A5_fout_v_B_lijst = []

    for row in A5_B:
        column = row.split(',')

        if column[0] != 'A5_papier_lijst':
            A5_papier_lijst.append(int(column[0]))
            A5_coefficienten_1_h_B_lijst.append(np.sqrt(float(column[1])))
            A5_fout_coefficienten_1_h_B_lijst.append(float(column[2]))
            A5_coefficienten_1_v_B_lijst.append(float(column[3]))
            A5_fout_coefficienten_1_v_B_lijst.append(float(column[4]))
    
    for papier in range(0, int(len(A5_papier_lijst) - 1)):
        if A5_papier_lijst[papier] == A5_papier_lijst[papier + 1]:
            A5_compressed_papier_lijst.append(A5_papier_lijst[papier])
            A5_temp_h_B_list = [A5_coefficienten_1_h_B_lijst[papier], A5_coefficienten_1_h_B_lijst[papier + 1]]
            A5_fout_temp_h_B_list = [A5_fout_coefficienten_1_h_B_lijst[papier], A5_fout_coefficienten_1_h_B_lijst[papier + 1]]
            A5_avg_h_B_lijst.append(float(np.mean(A5_temp_h_B_list)))
            A5_fout_h_B_lijst.append(float(np.sqrt(np.std(A5_temp_h_B_list) + np.var(A5_fout_temp_h_B_list))))
            A5_temp_v_B_list = [A5_coefficienten_1_v_B_lijst[papier], A5_coefficienten_1_v_B_lijst[papier + 1]]
            A5_fout_temp_v_B_list = [A5_fout_coefficienten_1_v_B_lijst[papier], A5_fout_coefficienten_1_v_B_lijst[papier + 1]]
            A5_avg_v_B_lijst.append(float(np.mean(A5_temp_v_B_list)))
            A5_fout_v_B_lijst.append(float(np.sqrt(np.std(A5_temp_v_B_list) + np.var(A5_fout_temp_v_B_list))))
        

    A5_B_CSV.close()


with A5_O_CSV as A5_O:
    A5_papier_lijst = []
    A5_coefficienten_1_h_O_lijst = []
    A5_fout_coefficienten_1_h_O_lijst = []
    A5_coefficienten_1_v_O_lijst = []
    A5_fout_coefficienten_1_v_O_lijst = []

    A5_compressed_papier_lijst = []
    A5_avg_h_O_lijst = []
    A5_fout_h_O_lijst = []
    A5_avg_v_O_lijst = []
    A5_fout_v_O_lijst = []

    for row in A5_O:
        column = row.split(',')

        if column[0] != 'A5_papier_lijst':
            A5_papier_lijst.append(int(column[0]))
            A5_coefficienten_1_h_O_lijst.append(np.sqrt(float(column[1])))
            A5_fout_coefficienten_1_h_O_lijst.append(float(column[2]))
            A5_coefficienten_1_v_O_lijst.append(float(column[3]))
            A5_fout_coefficienten_1_v_O_lijst.append(float(column[4]))
    
    for papier in range(0, int(len(A5_papier_lijst) - 1)):
        if A5_papier_lijst[papier] == A5_papier_lijst[papier + 1]:
            A5_compressed_papier_lijst.append(A5_papier_lijst[papier])
            A5_temp_h_O_list = [A5_coefficienten_1_h_O_lijst[papier], A5_coefficienten_1_h_O_lijst[papier + 1]]
            A5_fout_temp_h_O_list = [A5_fout_coefficienten_1_h_O_lijst[papier], A5_fout_coefficienten_1_h_O_lijst[papier + 1]]
            A5_avg_h_O_lijst.append(float(np.mean(A5_temp_h_O_list)))
            A5_fout_h_O_lijst.append(float(np.sqrt(np.std(A5_temp_h_O_list) + np.var(A5_fout_temp_h_O_list))))
            A5_temp_v_O_list = [A5_coefficienten_1_v_O_lijst[papier], A5_coefficienten_1_v_O_lijst[papier + 1]]
            A5_fout_temp_v_O_list = [A5_fout_coefficienten_1_v_O_lijst[papier], A5_fout_coefficienten_1_v_O_lijst[papier + 1]]
            A5_avg_v_O_lijst.append(float(np.mean(A5_temp_v_O_list)))
            A5_fout_v_O_lijst.append(float(np.sqrt(np.std(A5_temp_v_O_list) + np.var(A5_fout_temp_v_O_list))))
        

    A5_O_CSV.close()


plt.figure(1, figsize=(15, 5))
plt.suptitle('A4 and A5 format combined. Restitutioncoefficient, calculated with h1/h0 and v1/v0. Average of all measurements with standard deviation')
plt.subplot(121)
plt.title('h1/h0 calculation')
plt.errorbar(A4_compressed_papier_lijst, A4_avg_h_lijst, yerr=A4_fout_h_lijst, capsize=2, fmt='o', ecolor = "black", label='A4 data and standard deviation', markersize='3')
plt.errorbar(A5_compressed_papier_lijst, A5_avg_h_B_lijst, yerr=A5_fout_h_B_lijst, capsize=2, fmt='o', ecolor = "black", label='A5 data and standard deviation', markersize='3')
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
plt.legend()
plt.subplot(122)
plt.title('v1/v0 calculation')
plt.errorbar(A4_compressed_papier_lijst, A4_avg_v_lijst, yerr=A4_fout_v_lijst, capsize=2, fmt='o', ecolor = "black", label='A4 data and standard deviation', markersize='3')
plt.errorbar(A5_compressed_papier_lijst, A5_avg_v_B_lijst, yerr=A5_fout_v_B_lijst, capsize=2, fmt='o', ecolor = "black", label='A5 data and standard deviation', markersize='3')
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
plt.ylim(0.1, 0.8)
plt.legend()
plt.savefig('A4_AND_A5_COR_AVG_SIGMA')


plt.figure(2, figsize=(15, 5))
plt.suptitle('A5 format, dropped from half the height of original measurements. Restitutioncoefficient, calculated with h1/h0 and v1/v0. Average of all measurements with standard deviation')
plt.subplot(221)
plt.title('h1/h0 calculation')
plt.errorbar(A5_compressed_papier_lijst, A5_avg_h_O_lijst, yerr=A5_fout_h_O_lijst, capsize=2, fmt='o', ecolor = "black", label='A5', markersize='3', color='darkorange')
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
plt.legend()
plt.subplot(222)
plt.title('v1/v0 calculation')
plt.errorbar(A5_compressed_papier_lijst, A5_avg_v_O_lijst, yerr=A5_fout_v_O_lijst, capsize=2, fmt='o', ecolor = "black", label='A5', markersize='3', color='darkorange')
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
plt.ylim(0.4, 0.7)
plt.legend()
plt.savefig('A5_COR_LOW_AVG_SIGMA')


plt.figure(3, figsize=(15, 5))
plt.subplot(321)
# plt.plot(A4_compressed_papier_lijst, A4_avg_h_lijst, 'o')
plt.plot(A4_papier_lijst, A4_coefficienten_1_h_lijst, 'o')
# plt.errorbar(A4_papier_lijst, A4_coefficienten_1_h_lijst, yerr=A4_fout_coefficienten_1_h_lijst, capsize=3, fmt='o', ecolor = "black", label='A4', markersize='5', color='darkorange')
plt.subplot(322)
# plt.errorbar(A4_papier_lijst, A4_coefficienten_1_v_lijst, yerr=A4_fout_coefficienten_1_v_lijst, capsize=3, fmt='o', ecolor = "black", label='A4', markersize='5', color='darkorange')
# plt.plot(A4_compressed_papier_lijst, A4_avg_v_lijst, 'o')
plt.plot(A4_papier_lijst, A4_coefficienten_1_v_lijst, 'o')

plt.figure(4, figsize=(15, 5))
plt.subplot(421)
# plt.errorbar(A5_papier_lijst, A5_coefficienten_1_h_B_lijst, yerr=A5_fout_coefficienten_1_h_B_lijst, capsize=3, fmt='o', ecolor = "black", label='A5', markersize='5', color='darkorange')
plt.plot(A5_papier_lijst, A5_coefficienten_1_h_B_lijst, 'o')
plt.subplot(422)
# plt.errorbar(A5_papier_lijst, A5_coefficienten_1_v_B_lijst, yerr=A5_fout_coefficienten_1_v_B_lijst, capsize=3, fmt='o', ecolor = "black", label='A5', markersize='5', color='darkorange')
plt.plot(A5_papier_lijst, A5_coefficienten_1_v_B_lijst, 'o')

plt.figure(5, figsize=(15, 5))
plt.subplot(521)
plt.plot(A5_papier_lijst, A5_coefficienten_1_h_O_lijst, 'o')
# plt.errorbar(A5_papier_lijst, A5_coefficienten_1_h_O_lijst, yerr=A5_fout_coefficienten_1_h_O_lijst, capsize=3, fmt='o', ecolor = "black", label='A5', markersize='5', color='darkorange')
plt.subplot(522)
# plt.errorbar(A5_papier_lijst, A5_coefficienten_1_v_O_lijst, yerr=A5_fout_coefficienten_1_v_O_lijst, capsize=3, fmt='o', ecolor = "black", label='A5', markersize='5', color='darkorange')
plt.plot(A5_papier_lijst, A5_coefficienten_1_v_O_lijst, 'o')


plt.show()