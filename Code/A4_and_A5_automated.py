# Naam: Saladin Shah
# Studentnummer: 15817490


import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv as csv


A4_test_max_snelheid = []
A4_test_minimale_hoogte = []

A4_coefficienten_1_h_lijst = []
A4_coefficienten_2_h_lijst = []
A4_coefficienten_3_h_lijst = []

A4_coefficienten_1_v_lijst = []
A4_coefficienten_2_v_lijst = []
A4_coefficienten_3_v_lijst = []


a_lijst = [1, 2, 3]
b_lijst = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 30, 40, 45, 50, 55, 60, 100, 140, 200, 240, 300, 340]
A4_papier_lijst = []

for b in b_lijst:
  for a in a_lijst:
        with open(f'E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4 Medium knikker (blauw)/{a}-{b}-M.csv', 'r') as yurr:
            hoogte_lijst = []
            frame_lijst = []
            frame_delta = 0
            teller = 0
            stuiteraantal = 0
            delta_hoogte = 600

            for regel in yurr:
                data_opgeknipt = regel.strip().split()

                if teller == 3:
                    print()
                else:    
                    if data_opgeknipt and data_opgeknipt[0] != 'Frame':
                        if data_opgeknipt and data_opgeknipt[0] != 'Tracks':
                            if data_opgeknipt and data_opgeknipt[0] != 'Track':
                                if float(data_opgeknipt[2]) < 60:
                                    frame_delta = int(data_opgeknipt[0])
                                    if float(data_opgeknipt[2]) < delta_hoogte:
                                        delta_hoogte = float(data_opgeknipt[2])
                                        echte_hoogte = 678.43695 - float(data_opgeknipt[2])
                                else:
                                    frame = int(data_opgeknipt[0]) - frame_delta
                                    y1 = float(data_opgeknipt[2])
                                    hoogte = 678.43695 - y1

                                    frame_lijst.append(frame)
                                    hoogte_lijst.append(hoogte)
                            else:
                                teller +=1
                        else:
                            teller +=1
                    else:
                        teller +=1


            # Snelheden berekenen (voor bepaling van toppen)
            snelheden = []

            for i in range(0, len(hoogte_lijst)):
                dy = hoogte_lijst[i] - hoogte_lijst[i - 1]
                dt = frame_lijst[i] - frame_lijst[i - 1]
                snelheid = dy / dt if dt != 0 else 0
                snelheden.append(snelheid)


            # Toppen detecteren: waar snelheid verandert van positief naar negatief
            maxima_frames = [0]
            maxima_hoogtes = [echte_hoogte]
            impact_frames = []
            impact_snelheden = []

            for i in range(0, len(snelheden)):
                if snelheden[i - 1] > 0 and snelheden[i] < 0 and len(maxima_frames) <= 3 and i > 20:  # filter op realistische waarde
                    maxima_frames.append(i)
                    maxima_hoogtes.append(hoogte_lijst[i])
                if snelheden[i - 1] < 0 and snelheden[i] > 0 and len(impact_snelheden) <= 3 and i > 20:
                    impact_snelheden.append(abs(snelheden[i - 4]))
                    impact_snelheden.append(snelheden[i + 1])
                    impact_frames.append(i - 4)
                    impact_frames.append(i + 1)

            print(f'maximum points zijn {maxima_frames}')
            print(f'maximum hoogtes zijn {maxima_hoogtes}')


            # Restitutiecoëfficiënten berekenen: hoogte_n / hoogte_(n-1)
            coefficienten_h = []
            cor1_h = maxima_hoogtes[1] / maxima_hoogtes[0]
            cor2_h = maxima_hoogtes[2] / maxima_hoogtes[1]
            # cor3_h = maxima_hoogtes[3] / maxima_hoogtes[2]

            coefficienten_v = []
            cor1_v = impact_snelheden[1] / impact_snelheden[0]
            cor2_v = impact_snelheden[3] / impact_snelheden[2]
            # cor3_v = impact_snelheden[3] / impact_snelheden[2]

            A4_coefficienten_1_h_lijst.append(cor1_h)
            A4_coefficienten_2_h_lijst.append(cor2_h)
            # A4_coefficienten_3_lijst.append(cor3_h)

            A4_coefficienten_1_v_lijst.append(cor1_v)
            A4_coefficienten_2_v_lijst.append(cor2_v)
            # A4_coefficienten_3_v_lijst.append(cor3_v)

            plt.figure(1, figsize=(15, 15))
            plt.suptitle('A4 Format. Position and speed graphs, of all measurements combined (messy)')
            plt.subplot(311)
            plt.title('Height over time, all measurements')
            plt.plot(frame_lijst, hoogte_lijst, label=b)
            plt.xlabel('Time (frames)')
            plt.ylabel('Height (px)')
            # plt.legend()
            # plt.show()
          
            plt.subplot(312)
            plt.title('Speed over time, all measurements')
            plt.plot(frame_lijst, snelheden, label=b)
            plt.xlabel('Time (frames)')
            plt.ylabel('Speed (px/frame)')
            # plt.xlim(0, 400)
            # plt.ylim(-20, 20)
            plt.savefig('A4_COMBINED_AUTOMATED_POS_AND_SPEED.png')

            A4_test_max_snelheid.append(max(snelheden))
            # print(cor1, cor2, cor3)
            A4_test_minimale_hoogte.append(min(hoogte_lijst))
            
            print(f'impact frames zijn: {impact_frames}')
            print(f'impact snelheden zijn: {impact_snelheden}')
            print(f'File: {a}-{b}')
            
            A4_papier_lijst.append(b)

# print(impact_snelheden)


print(min(A4_test_minimale_hoogte))
print(max(A4_test_max_snelheid))


A5_test_max_snelheid = []
A5_test_minimale_hoogte = []

A5_coefficienten_1_h_B_lijst = []
A5_coefficienten_2_h_B_lijst = []
A5_coefficienten_3_h_B_lijst = []

A5_coefficienten_1_v_B_lijst = []
A5_coefficienten_2_v_B_lijst = []
A5_coefficienten_3_v_B_lijst = []

A5_coefficienten_1_h_O_lijst = []
A5_coefficienten_2_h_O_lijst = []
A5_coefficienten_3_h_O_lijst = []

A5_coefficienten_1_v_O_lijst = []
A5_coefficienten_2_v_O_lijst = []
A5_coefficienten_3_v_O_lijst = []


a_lijst = [1, 2]
b_lijst = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52, 54, 56, 58, 60, 100, 150, 200, 250, 300]
h_lijst = ['B', 'O']
A5_papier_lijst = []

for b in b_lijst:
    for a in a_lijst:
        A5_papier_lijst.append(b)
        # for h in h_lijst:
        with open(f'E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5 Medium knikker (blauw)/{a}-{b}-B-A5.csv', 'r') as yurr:
            hoogte_lijst = []
            frame_lijst = []
            frame_delta = 0
            teller = 0
            stuiteraantal = 0
            delta_hoogte = 600


            for regel in yurr:
                data_opgeknipt = regel.strip().split()

                if teller == 3:
                    print()
                else:    
                    if data_opgeknipt and data_opgeknipt[0] != 'Frame':
                        if data_opgeknipt and data_opgeknipt[0] != 'Tracks':
                            if data_opgeknipt and data_opgeknipt[0] != 'Track':
                                if float(data_opgeknipt[2]) < 60:
                                    frame_delta = int(data_opgeknipt[0])
                                    if float(data_opgeknipt[2]) < delta_hoogte:
                                        delta_hoogte = float(data_opgeknipt[2])
                                        echte_hoogte = 639.0202 - float(data_opgeknipt[2])
                                else:
                                    frame = int(data_opgeknipt[0]) - frame_delta
                                    y1 = float(data_opgeknipt[2])
                                    hoogte = 639.0202 - y1

                                    frame_lijst.append(frame)
                                    hoogte_lijst.append(hoogte)
                            else:
                                teller +=1
                        else:
                            teller +=1
                    else:
                        teller +=1


            # Snelheden berekenen (voor bepaling van toppen)
            snelheden = []

            for i in range(0, len(hoogte_lijst)):
                dy = hoogte_lijst[i] - hoogte_lijst[i - 1]
                dt = frame_lijst[i] - frame_lijst[i - 1]
                snelheid = dy / dt if dt != 0 else 0
                snelheden.append(snelheid)


            # Toppen detecteren: waar snelheid verandert van positief naar negatief
            maxima_frames = [0]
            maxima_hoogtes = [echte_hoogte]
            impact_frames = []
            impact_snelheden = []
            for i in range(0, len(snelheden)):
                if snelheden[i - 1] > 0 and snelheden[i] < 0 and len(maxima_frames) <= 3 and i > 40:  # filter op realistische waarde
                    maxima_frames.append(i)
                    maxima_hoogtes.append(hoogte_lijst[i])
                if snelheden[i - 1] < 0 and snelheden[i] > 0 and len(impact_snelheden) <= 3 and i > 40:
                    impact_snelheden.append(abs(snelheden[i - 4]))
                    impact_snelheden.append(snelheden[i + 1])
                    impact_frames.append(i - 4)
                    impact_frames.append(i + 1)

            print(f'maximum points zijn {maxima_frames}')
            print(f'maximum hoogtes zijn {maxima_hoogtes}')


            # Restitutiecoëfficiënten berekenen: hoogte_n / hoogte_(n-1)
            coefficienten_h = []
            cor1_h = maxima_hoogtes[1] / maxima_hoogtes[0]
            cor2_h = maxima_hoogtes[2] / maxima_hoogtes[1]
            # cor3_h = maxima_hoogtes[3] / maxima_hoogtes[2]

            coefficienten_v = []
            cor1_v = impact_snelheden[1] / impact_snelheden[0]
            cor2_v = impact_snelheden[3] / impact_snelheden[2]
            # cor3_v = impact_snelheden[3] / impact_snelheden[2]

            # if h == 'B':
            A5_coefficienten_1_h_B_lijst.append(cor1_h)
            A5_coefficienten_2_h_B_lijst.append(cor2_h)
            # A5_coefficienten_3_lijst.append(cor3_h)

            A5_coefficienten_1_v_B_lijst.append(cor1_v)
            A5_coefficienten_2_v_B_lijst.append(cor2_v)
            # A5_coefficienten_3_v_lijst.append(cor3_v)
            # else:
            #     coefficienten_1_h_O_lijst.append(cor1_h)
            #     coefficienten_2_h_O_lijst.append(cor2_h)
            #     # coefficienten_3_lijst.append(cor3_h)

            #     coefficienten_1_v_O_lijst.append(cor1_v)
            #     coefficienten_2_v_O_lijst.append(cor2_v)
            #     # coefficienten_3_v_lijst.append(cor3_v) 

        plt.figure(2, figsize=(15, 15))
        plt.suptitle('A5 Format. Position and speed graphs, of all measurements combined (messy)')
        plt.subplot(311)
        plt.title('Height over time, all measurements')
        plt.plot(frame_lijst, hoogte_lijst)
        plt.xlabel('Time (frames)')
        plt.ylabel('Height (px)')
        
        plt.subplot(312)
        plt.title('Speed over time, all measurements')
        plt.plot(frame_lijst, snelheden)
        plt.xlabel('Time (frames)')
        plt.ylabel('Speed (px/frame)')
        # plt.xlim(0, 400)
        # plt.ylim(-20, 20)
        plt.savefig('A5_COMBINED_AUTOMATED_POS_AND_SPEED.png')

        A5_test_max_snelheid.append(max(snelheden))
        # print(cor1, cor2, cor3)
        A5_test_minimale_hoogte.append(min(hoogte_lijst))
        
        print(impact_frames)
        print(impact_snelheden)
        print(f'File: {a}-{b}-B')

# print(impact_snelheden)

plt.figure(3, figsize=(15, 10))
plt.suptitle('A4 and A5 combined. CoR against amount of paper pages, all measurements')
plt.subplot(321)
plt.title('CoR calculated with height ratio (h_after_bounce / h_initial)')
plt.plot(A4_papier_lijst, A4_coefficienten_1_h_lijst, 'o', label='A4, h1/h0 (first bounce)', markersize= '3')
plt.plot(A5_papier_lijst, A5_coefficienten_1_h_B_lijst, 'o', label='A5, h1/h0 (first bounce)', markersize= '3')
# plt.plot(papier_lijst, coefficienten_2_h_B_lijst, 'o', label='h2/h1 (second bounce)')
# plt.plot(papier_lijst, coefficienten_3_h_lijst, label='h3/h2 (third bounce)')
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
# plt.ylim(0, 0.6)
plt.legend()

plt.subplot(322)
plt.title('CoR calculated with speed ratio (v_after_impact / v_before_impact)')
plt.plot(A4_papier_lijst, A4_coefficienten_1_v_lijst, 'o', label='A4, v1/v0 (first impact)', markersize= '3')
plt.plot(A5_papier_lijst, A5_coefficienten_1_v_B_lijst, 'o', label='A5, v1/v0 (first impact)', markersize= '3')
# plt.plot(papier_lijst, coefficienten_2_v_B_lijst, 'o', label='v2/v1 (second impact)')
# plt.plot(papier_lijst, coefficienten_3_v_lijst, label='v3/v2 (third impact)')
# plt.ylim(0, 0.6)
plt.xlabel('# of paper pages (amount)')
plt.ylabel('Restitutioncoefficient (ratio)')
plt.legend()
plt.savefig('A4_AND_A5_B_AUTOMATED_COR.png')
plt.show()


# plt.figure(3, figsize=(15, 10))
# plt.suptitle('A5 Format. CoR against amount of paper pages,with "low" starting height, all measurements')
# plt.subplot(331)
# plt.title('CoR calculated with height ratio (h_after_bounce / h_initial)')
# plt.plot(papier_lijst, coefficienten_1_h_O_lijst, 'o', label='h1/h0 (first bounce)')
# # plt.plot(papier_lijst, coefficienten_2_h_B_lijst, 'o', label='h2/h1 (second bounce)')
# # plt.plot(papier_lijst, coefficienten_3_h_lijst, label='h3/h2 (third bounce)')
# plt.xlabel('# of paper pages (amount)')
# plt.ylabel('Restitutioncoefficient (ratio)')
# plt.ylim(0, 0.6)
# plt.legend()


# plt.subplot(332)
# plt.title('CoR calculated with speed ratio (v_after_impact / v_before_impact)')
# plt.plot(papier_lijst, coefficienten_1_v_O_lijst, 'o', label='v1/v0 (first impact)')
# # plt.plot(papier_lijst, coefficienten_2_v_O_lijst, 'o', label='v2/v1 (second impact)')
# # plt.plot(papier_lijst, coefficienten_3_v_lijst, label='v3/v2 (third impact)')
# plt.xlabel('# of paper pages (amount)')
# plt.ylabel('Restitutioncoefficient (ratio)')
# plt.ylim(0, 0.6)
# plt.legend()
# plt.savefig('A5_AUTOMATED_COR_LOW.png')
# plt.show()


print(min(A5_test_minimale_hoogte))
print(max(A5_test_max_snelheid))


# with open(f'E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4_sanitized_data.csv', 'w'):
# matrix = []
# for i in range(0, len(A4_papier_lijst)):
#     matrix.append([A4_papier_lijst[i], A4_coefficienten_1_h_lijst[i]])

# print(matrix)

import csv

with open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4_sanitized_data.csv', 'w', newline='') as A4writer:
    writer = csv.writer(A4writer)
    header = ["A4_papier_lijst", "A4_coefficienten_1_h_lijst"]

    writer.writerow(header)
    for i in range(0, len(A4_papier_lijst)):
        writer.writerow([A4_papier_lijst[i], A4_coefficienten_1_h_lijst[i]])
    open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A4_sanitized_data.csv', 'w', newline='').close()


with open('E:/Documents/GitHub/2025-Projects_Team-1-Bouncing-on-Paper-The-Surprising-Restitution-Coefficient-of-a-Paper-Stack-/Code/A5_sanitized_data.csv', 'w', newline='') as A5writer:
    writer = csv.writer(A5writer)
    header = ["A5_papier_lijst", "A5_coefficienten_1_h_lijst"]

    writer.writerow(header)
    for i in range(0, len(A5_papier_lijst)):
        writer.writerow([A5_papier_lijst[i], A5_coefficienten_1_h_B_lijst[i]])