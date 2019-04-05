from time import time
from decimal import Decimal
from random import randint
from random import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plota_grafico(averages):
    plt.ylabel('Media de Tempo')

    for key in averages.keys():
        plt.bar(key, averages[key])

    plt.show()

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} wins)".format(pct, absolute)

def plota_grafico_pizza(wins):
    labels = wins.keys()
    valores = list(wins.values())
    ax = plt.subplots(figsize=(12, 9), subplot_kw=dict(aspect="equal"))[1]
    wedges, texts, autotexts = ax.pie(valores, autopct=lambda pct: func(pct, valores), textprops=dict(color="w"))
    ax.legend(wedges, labels, title="Algoritimos", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("Algoritimos de Busca")
    plt.show()

def calc_media(results):
    averages = {}

    for key in results.keys():
        averages[key] = sum(results[key]) / len(results[key])
    return averages

def cria_lista_sem_repeticao(tamanho):
    return random.sample(range(0, tamanho + 1), tamanho)

def cria_lista_com_repeticao(tamanho, inicio_intervalo, fim_intervalo):
    return [random.randint(inicio_intervalo, fim_intervalo) for x in range(tamanho)]

def insertion_sort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
    return alist

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def selection_sort(alist):
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
    return alist

if __name__ == '__main__':
    results = {'Selection': [], 'Insertion': [], 'Bubble': []}
    result = {'Selection': 0, 'Insertion': 0, 'Bubble': 0}
    wins = {'Selection': 0, 'Insertion': 0, 'Bubble': 0}
    