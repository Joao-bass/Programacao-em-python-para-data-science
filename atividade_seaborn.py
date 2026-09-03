import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_excel('vendas.slsx')

print(df)

media = df['Vendas'].mean()
print('Media',media)

df = ['Variacao']= df['Vendas'].pct_change()
print(df)

sns.lineplot(data= df, x= 'Meses', y='Vendas')

plt.show()
