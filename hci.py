import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd

pd.set_option('display.max_columns', None) 

dane = pd.read_csv(r"/Users/dawidczech/Desktop/dane2.csv", delimiter=';', engine='python') 
kanal1=dane["pierwsza"]
numer=dane["Liczba"]

czestProbkowania = 200
t=np.linspace(0, 37.96, 200*37.96)

przefiltrowany1 = ag.pasmowozaporowy(kanal1, czestProbkowania, 49,51)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany1, czestProbkowania, 1,50)

plt.subplot(2, 1, 1)
plt.plot(t,kanal1[:int(200*37.96)]) #to wyświetla pełen sygnał naszej osoby
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')

plt.subplot(2, 1, 2)
plt.plot(t,przefiltrowany2[:int(200*37.96)]) #to wyświetla przefiltrowany
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')

plt.show()

print("Osoba badana mrugnęła przy tych cyferkach: ")

for i in range (7593):
    if przefiltrowany2[i]>0.1: #wartość progowa mrugnięcia
        print(numer[i])

