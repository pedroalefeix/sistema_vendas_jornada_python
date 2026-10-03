# Título - Sistema de Vendas
# Seção Cadastrar Vendas
  # Campo Data
  # Campo Vendedor
  # Campo Produto
  # Campo Quantidade
  # Campo Valor
  # Campo Cadastrar Venda
    # quando clicar no botão -> adicionar a venda na tabela
# Seção Vendas Cadastradas
  # Tabela com as Vendas
# Seção Dashboard
  # Card/Métrica -> Faturamento Total
  # Gráfico de Barra/Coluna -> Venda por vendedor
  # Gráfico de Pizza -> Venda por produto

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica de cadastro
if botao_cadastrar:
  nova_venda = [str(data), vendedor, produto, quantidade, valor]
  ultima_linha = len(tabela_vendas)
  tabela_vendas.loc[ultima_linha] = nova_venda
  tabela_vendas.to_csv("vendas.csv", index=False)
  st.success("Venda cadastrada!")

# Seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Seção de dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento:.2f}")

# Gráfico de Barra/Coluna -> Venda por vendedor
grafico_barra = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico_barra)

# Gráfico de Pizza -> Venda por produto
grafico_pizza =px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico_pizza)