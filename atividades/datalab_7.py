import pandas as pd

df_bruto = pd.read_excel('/Users/lucas/Desktop/inteligencia_de_mercado/ime/Inteligencia_de_mercado/atividades/arquivos_suporte/ime_datalab7_dados_financeiros.xlsx')

colunas_data = df_bruto.columns[2:]
 
# Transformar para formato longo
df = df_bruto.melt(
    id_vars=["Tipo", "Componente"],
    value_vars=colunas_data,
    var_name="Data",
    value_name="Valor"
)
 
# Converter valores: substituir vírgula por ponto e converter para float
df["Valor"] = df["Valor"].astype(str).str.replace(",", ".").astype(float)
 
# Converter coluna de data para datetime e extrair o Ano
df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
df["Ano"] = df["Data"].dt.year
 
# 1. Total de Receitas

total_receitas = df[df["Tipo"] == "Receitas"]["Valor"].sum() 
print(f"R$ {total_receitas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
 

# 2. TOTAL DE DESPESAS

 
total_despesas = df[df["Tipo"] == "Despesas"]["Valor"].sum()
print(f"R$ {total_despesas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
 
# 3. MARGEM DE LUCRO
 
lucro = total_receitas - total_despesas
margem_lucro = (lucro / total_receitas) * 100 
print(f"Lucro Total : R$ {lucro:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Margem de Lucro: {margem_lucro:.2f}%")
 
# 4. TOTAL DE RECEITAS POR COMPONENTE
 
receitas_por_componente = (
    df[df["Tipo"] == "Receitas"]
    .groupby("Componente")["Valor"]
    .sum()
    .sort_values(ascending=False)
) 
for componente, valor in receitas_por_componente.items():
    print(f"  {componente:<20} R$ {valor:>12,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
 
# 5. TOTAL DE DESPESAS POR COMPONENTE VS. MÉDIA
 
despesas_por_componente = (
    df[df["Tipo"] == "Despesas"]
    .groupby("Componente")["Valor"]
    .sum()
)
 
media_despesas = despesas_por_componente.mean()
print(f"  Média de Despesas por Componente: R$ {media_despesas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
for componente, valor in despesas_por_componente.sort_values(ascending=False).items():
    diff = valor - media_despesas
    sinal = "+" if diff >= 0 else ""
    print(f"  {componente:<20} R$ {valor:>12,.2f}  ({sinal}{diff:,.2f} vs. média)".replace(",", "X").replace(".", ",").replace("X", "."))
 
# 6. RECEITAS E DESPESAS POR COMPONENTE E ANO
 
tabela_hierarquica = (
    df.groupby(["Tipo", "Componente", "Ano"])["Valor"]
    .sum()
    .reset_index()
    .sort_values(["Tipo", "Componente", "Ano"])
)
 
tipo_atual = None
componente_atual = None
for _, linha in tabela_hierarquica.iterrows():
    if linha["Tipo"] != tipo_atual:
        tipo_atual = linha["Tipo"]
        print(f"\n  [{tipo_atual}]")
    if linha["Componente"] != componente_atual:
        componente_atual = linha["Componente"]
        print(f"    {componente_atual}")
    valor_fmt = f"R$ {linha['Valor']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"      {int(linha['Ano'])}: {valor_fmt}")
 
# 7. SEGMENTOS COM MAIORES E MENORES RECEITAS E DESPESAS
 
# Receitas
print(f"  Maior  -> {receitas_por_componente.idxmax()}: R$ {receitas_por_componente.max():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"  Menor  -> {receitas_por_componente.idxmin()}: R$ {receitas_por_componente.min():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
 
# Despesas
print(f"  Maior  -> {despesas_por_componente.idxmax()}: R$ {despesas_por_componente.max():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"  Menor  -> {despesas_por_componente.idxmin()}: R$ {despesas_por_componente.min():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))