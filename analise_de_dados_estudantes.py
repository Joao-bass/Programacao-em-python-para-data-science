import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('dados_estudantes.csv')
df = pd.DataFrame(dados)



# 1 - Crie um gráfico de notas por genero
dados_agrupados = df.groupby('gender')['exam_score'].mean()

genero = dados_agrupados.index
notas = dados_agrupados.values

plt.figure(figsize=(6,6))
plt.bar(genero,notas,  color = 'green')

plt.xlabel('Genero')
plt.ylabel('Nota media')
plt.title('Medias de notas por genero')
plt.show()




# 2 - Gráfico de horas de estudos x notas
dados_2 = df.groupby('study_hours_per_day')['exam_score'].mean()

horas = dados_2.index
nota = dados_2.values

plt.scatter(horas, nota, color = 'red')
plt.xlabel('Horas de estudo')
plt.ylabel('Notas')
plt.title('1')
plt.show()


# 3 -  Média de notas por idade
media = df.groupby('age')['exam_score'].mean()
print(media)



# 4 - Analise: Média de horas por estudos
media_hora = df['study_hours_per_day'].mean()
df['media_hora'] = media_hora
print(media_hora)




# 5 - Analise: Média de horas por estudos
notas_idade = df.groupby()