 # Disciplina: Inteligencia de Mercado e Analytics (ibm0115)
 # DataLab2 (objetivo): Analise de serie temporal com python
 # Autor: Lucas Barreto
 # Data: 02/03/2026

# importando bibliotecas necessárias
import matplotlib.pyplot as plt
import pandas as pd
import ipeadatapy as ipd

# Definir vetor para armanzenar uma serie historica

count = 73
#print("Minha variavel: ", count)

anos_observados = [0] * count


ano_inicial = 1952

# preenche o vetor que armazena a minha seria historica
for x in range(count):
  anos_observados[x] = ano_inicial + x

#print(anos_observados)

# seleciona no vetor os desejados
anos_selecionados = [0] * 20
#print(anos_selecionados)

# preenche o vetor dos anos selecionados
i = 0
for x in anos_observados:
  if x >= 2005:
    anos_selecionados[i] = x
    i = i + 1


# escolhendo a serie historica de interesse
serie_escolhida = ipd.timeseries('ELETRO_CEET')

# limitando a 15 observações a partir de 2010
serie_15_anos = serie_escolhida.tail(20).copy()

valores = serie_15_anos['VALUE (GWh)'].tolist()
print(valores)

df_dados = pd.DataFrame({"ano": anos_selecionados, "consumo": valores})
print(df_dados)

# plotando o gráfico para visualizar a serie historica
plt.plot(df_dados['ano'], df_dados['consumo'])
plt.xlabel('Ano')
plt.ylabel('Consumo (GWh)')
plt.title('Consumo de Energia Elétrica (2005-2024)')
plt.grid()
plt.show()