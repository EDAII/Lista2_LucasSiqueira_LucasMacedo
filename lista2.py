from time import time
from decimal import Decimal
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

TAM_LISTA = 100
NUM_REPETICOES = 1000 
INICIO_INTERVALO = 0
FIM_INTERVALO = 2000

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

def cria_lista_sem_repeticao():
    return random.sample(range(0, TAM_LISTA + 1), TAM_LISTA)

def cria_lista_com_repeticao():
    return [random.randint(INICIO_INTERVALO, FIM_INTERVALO) for x in range(TAM_LISTA)]

def insertion_sort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selection_sort(alist):
    for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

if __name__ == '__main__':
    results = {'Selection': [], 'Insertion': [], 'Bubble': []}
    result = {'Selection': 0, 'Insertion': 0, 'Bubble': 0}
    wins = {'Selection': 0, 'Insertion': 0, 'Bubble': 0}
    verifica_empate = set()
    qtd_empates = 0

    for aux in range(NUM_REPETICOES):
        lista = cria_lista_sem_repeticao()
        lista_com_repeticao = cria_lista_com_repeticao()

        for key in result.keys():
            if key == 'Selection':
                inicio = time()
                # selection_sort(lista.copy())
                selection_sort(lista_com_repeticao.copy())
            elif key == 'Insertion':
                inicio = time()
                # insertion_sort(lista.copy())
                insertion_sort(lista_com_repeticao.copy())
            else: 
                inicio = time()
                # bubble_sort(lista.copy())
                bubble_sort(lista_com_repeticao.copy())
    
            fim = time()
            tempo = Decimal(fim - inicio)

            result[key] = tempo
            results[key].append(tempo)

            verifica_empate.add(tempo)

        if len(verifica_empate) != 3:
            qtd_empates += 1

        verifica_empate = set()
         
        lis = list(result.items())
        winner = min(lis,key=lambda item:item[1])

        wins[winner[0]] += 1



    print('Quantidade de empates: ', qtd_empates)

    averages = calc_media(results)

    print('\n\t \t \tResultado em Wins:')
    for key in wins.keys():
        print(key + ': ' + str(wins[key]))

    print('\n\t \t \tMedia de Tempo:')
    for key in averages.keys():
        print(key + ': ' + str(averages[key]))
    
    plota_grafico_pizza(wins)
    plota_grafico(averages)
    