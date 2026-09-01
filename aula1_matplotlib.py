import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
# import tkinter as tk



def analise():
    dados = pd.read_csv('dados.csv')
    anos  = dados['ano']
    venda = dados['vendas']
    df = pd.DataFrame(dados)
    

    #grafico pizza
    cor = ['red','orange','green']
    plt.figure(figsize = (6,6))
    plt.pie(df['vendas'], labels= df['ano'],autopct= '%1.1f%%')
    plt.show()

    #grafico pde barras
    plt.figure(figsize =  (6,6))
    plt.bar(df['ano'], df['lucro'])
    plt.show()

    #grafico de linha
    plt.figure(figsize= (7,10))
    plt.plot(df['ano'], df['vendas'], marker= 'o', linestyle= '-', color= 'green')
    plt.show()

    #grafico de correlacao
    plt.figure(figsize=(5,6))
    plt.scatter(df['vendas'], df['lucro'], color = 'orange')
    plt.grid(True)
    plt.show()



analise()



fig, ax  =  plt.subplots()#cria uma figura 
fig, ax = plt.subplot() #cria o axes


dados =  pd.read_csv('dados.csv')#le o arquivo
dados = pd.read_csv('dados.csv')
plt.title('Isso  é um titulo')#mostra o titulo
plt.title('INFORMACOES')

ax.bar(dados['nome'], dados['idade'])#trabalha com as colunas
ax.bar(dados['idade'], dados['nome'])
ax.set_xlabel('eixo X')#cria eixo
ax.set_ylabel('eixo Y')#eixo y


plt.show() #printa