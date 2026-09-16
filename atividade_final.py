import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('WorldCups.csv')
df = pd.DataFrame(dados)

df['Attendance'].str.replace('.','')
df['Attendance'] = df['Attendance'].str.replace('.','')

pd.to_numeric(df['Attendance'])
df['Attendance'] = pd.to_numeric(df['Attendance'])

media = df['GoalsScored'].mean()
mediana = df['GoalsScored'].median()
moda = df['GoalsScored'].mode()

print(f'''
    Em media foram marcados, {media} gols por edição de copa do mundo  
    
    A mediana foi, {mediana} gols, indicando que metade dos valores esta abaixo desse numero
    
    A moda apresentou 3 valores, {moda} 
''')

mais_vezes_segundo_lugar = df['Runners-Up'].value_counts().head(1)
print('A seleção que mais veses ficou em segundo lugar: ',mais_vezes_segundo_lugar)

maior_publico = df['Attendance'].max()
ano_maio_publico = df.loc[df['Attendance'] == maior_publico, 'Year']
print('O maior publico ja registrado em uma edicao de copa do mundo foi:',maior_publico)
print('Esse registro ocorreu no ANO de ',ano_maio_publico)

menor_numero_selecoes = df['QualifiedTeams'].min()
ano_menor = df.loc[df['QualifiedTeams'] == menor_numero_selecoes, 'Year']
print('A menor quantidade de seleçoes registrado em copas foi: ',menor_numero_selecoes)
print('Isso aconteceu no ano de ',ano_menor)












df.describe()