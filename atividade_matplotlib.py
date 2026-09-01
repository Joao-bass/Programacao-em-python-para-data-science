import matplotlib.pylab as plt
import pandas as pd
import numpy as np


def mostrar_plot():
    dados = pd.read_csv('d_vendas.csv')
    df = pd.DataFrame(dados)
   
    plt.figure(figsize=(6,4))
    plt.plot(df['ano'], df['vendas'], marker = 'o', color= 'green')
    plt.show()




def medias_barras():
    dados = pd.read_csv('media.csv')
    df = pd.DataFrame(dados)

    plt.figure(figsize=(7,5))
    plt.bar(df['meses'], df['m_jose'], color= 'black')
    plt.show()



mostrar_plot()
medias_barras() 
