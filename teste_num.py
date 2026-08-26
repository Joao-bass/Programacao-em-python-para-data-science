import numpy as np

dados = np.arange(0, 25).reshape(5,5)
np.random.shuffle(dados)

print('matriz original')
print(dados)
print('=' * 10)

for i in dados:
    media = np.mean(i)    
    maximo = np.max(i)
    minimo = np.min(i)

    print(f"Linha {i}:")
    print(f"A média é: {media} | O valor máximo: {maximo} | O valor mínimo: {minimo}")
    print('=' * 40)