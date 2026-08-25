import statistics


def calculos(frequencia):
    moda = statistics.mode(frequencia)
    media = statistics.mean(frequencia)
    mediana = statistics.median(frequencia)
    desvio = statistics.pstdev(frequencia)
    variancia = statistics.pvariance(frequencia)
    amplitude = max(frequencia) - min(frequencia)
    print('Moda = {:.2f}\nMedia = {:.2F}\nMediana = {:.2f}\nDesvio = {:.2f}\nAmplitude = {:.2f}\nVariancia = {:.2f}'.format(moda,media, mediana,desvio,amplitude,variancia))


empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa5 = [1200, 1500, 1800, 2500, 10000]

calculos(empresa1)
calculos(empresa2)
calculos(empresa3)
calculos(empresa4)
calculos(empresa5)





















# def cal_mediana():
#     frequencia = [1.5,6.8,9.7,10.6]
#     mediana = statistics.median(frequencia)
#     print(mediana)

# cal_mediana()

# def cal_media():
#     frequencia = [200,300,500,700,900,400,600]
#     media = statistics.mean(frequencia)
#     print('{:.3f}'.format(media))

# cal_media()






# amp = max() - min()
