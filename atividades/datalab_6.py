# instalação de pacotes
# !pip install numpy-financial

## Parametros do problema
# valor presente liquido
import numpy_financial as npf

valor_incial = -170000 # investimento inicial no projeto
valor_entrada_saida = 60000 - 10000

# teste
# vetor = [8, 9, 110, 50, 60]
# len(vetor)
# vetor

# contrói o vetor de fluxo de caixa
vetor_fluxo_caixa = [valor_incial,       # aporte inicial
                   valor_entrada_saida, # desembolsos de fluxo de caixa líquido (1-6)
                   valor_entrada_saida, # sendo igual ao seu período n
                   valor_entrada_saida,
                   valor_entrada_saida,
                   valor_entrada_saida,
                   valor_entrada_saida]

print(f"Fluxo de caixa analisado: {vetor_fluxo_caixa}")

# calcula o valor presente líquido (vpl) por meio da função
# npv() da biblioteca numpy_financial
vl_presente_liquido = npf.npv(rate=0.17, values=vetor_fluxo_caixa)

print(f"O Valor Presente Líquido (VPL) é: {round(vl_presente_liquido, 4)}")

# Cálculo da TIR (Tax Interna de Retorno)

# Parâmentros do problema
vl_aporte_inicial = -170000
valor_entrada_saida = 60000 - 10000

vetor_fluxo_caixa = np.zeros(7)
vetor_fluxo_caixa[0] = vl_aporte_inicial

# loop para preencher o vetor de fluxo de caixa
for i in range(6):
  vetor_fluxo_caixa[i+1] = valor_entrada_saida

print(vetor_fluxo_caixa)

# calcular a TIR por da biblioteca numpy_financial
vl_calculado_tir = npf.irr(vetor_fluxo_caixa)
print(vl_calculado_tir)
print("TIR = " + str(round(vl_calculado_tir*100, ndigits=2)) + "%")

# plotar o gráfico da analise da TIR
import matplotlib.pyplot as plt
import numpy as np

eixo_x = np.linspace(0,0.35,200)
VPL = np.array([npf.npv(i, vetor_fluxo_caixa) for i in eixo_x])

# construção do gráfico
print("Lucas Lemos Barreto (202301133271 - 30/03/26)")
plt.plot(eixo_x, VPL, '--k', linewidth=2)
plt.plot(vl_calculado_tir, 0, 'k*', markersize=15)
plt.xlabel('Juros - i')
plt.title("TIR - Análise da Taxa Interna de Retorno")
plt.grid()