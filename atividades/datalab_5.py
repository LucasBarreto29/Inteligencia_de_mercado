# Instalação de pacotes
# !pip install numpy-financial

## Parâmetros do problema
# Valor presente (vp)
# valor desejado no futuro (vf)
# taxa de juros de referência (r)
# número de período (n)

# cálculo do valor presente
def calcula_valor_presente(valor_futuro, tx_juros, nr_periodos):
  valor_presente = valor_futuro / (1 + tx_juros) ** nr_periodos
  return valor_presente

# versão pro
def calcula_valor_presente_pro(valor_futuro, tx_juros, nr_periodos):
  nr_denominador = (1 + tx_juros) ** nr_periodos

  if (nr_denominador > 0):
    valor_presente = valor_futuro / nr_denominador

  return valor_presente

# teste da função VP (valor de presente)
# Exemplo: quero ter 100.000 em 5 anos e a LTN com vencimento para 2032 está a 14,0% a.a.

valor_presente_calculado = calcula_valor_presente_pro(valor_futuro = 100000,
                                                      tx_juros = 0.14, # Taxa pré-fixado
                                                      nr_periodos = 5)
print(f"O valor prsente deve ser: {round(valor_presente_calculado,2)}")

# Simulação de cálculo de viabilidade de projetos

# Pode vir de onde?
# API do BACEN
# Baixar dataset
# Banco de dados
vetor_tx_juros = [12.38, 13.03, 10.89, 14.33]

nmr_periodos = 1
vl_futuro = 10000

for tx in vetor_tx_juros:
  vl_calculado = calcula_valor_presente_pro(vl_futuro, tx, nmr_periodos)
  print(f"O valor presente da taxa {tx} foi: {round(vl_calculado,4)}")