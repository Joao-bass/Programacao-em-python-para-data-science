import statistics 



def criar_notas():
    listas_nomes = ['ana', 'julia', 'fernanda', 'bernardo']
    notas_aluno = []
    for n in range(len(listas_nomes)):
        n1 = float(input('nota 1 >>'))
        n2 = float(input('nota 2 >>'))
        n3 = float(input('nota 3 >>'))
        notas_aluno.append([n1,n2,n3])
    return notas_aluno    
           



def analise():
        l_notas = criar_notas()

        todas_notas = []

        for n in l_notas:
              for nota in n:
                    todas_notas.append(nota)  
        media = statistics.mean(todas_notas)
        moda = statistics.mode(todas_notas)
        mediana = statistics.median(todas_notas)
        desvio = statistics.pstdev(todas_notas)
        variancia = statistics.pvariance(todas_notas)
        amplitude = max(todas_notas) - min(todas_notas)
        menor = min(todas_notas)
        maior = max(todas_notas)
        print(f'''
                media = {media}
                moda = {moda}
                mediana = {mediana}
                desvio padrao = {desvio}
                variancia = {variancia}
                amplitude = {amplitude}
                menor nota é: {menor}
                maior nota é: {maior}

                    
                ''')
       



    


analise()
