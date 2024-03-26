#inserção de dados:

import random

id = random.randint(1000, 9999)
nome = input("digite o nome do produto: ")
desc = input("digite a descrição do produto: ")
ca = float(input("digite o custo do produto: "))
cf = float(input("digite o custo fixo/administrativo: "))
cv = float(input("digite o valor da comissão de vendas: "))
iv = float(input("digite o valor do imposto sobre o produto: "))
ml = float(input("digite o valor da rentabilidade "))

#leitura de dados

import pandas as pd

dados = pd.read_csv("dados.csv")

nova_linha = pd.DataFrame({'ID': [id], 'Nome': [nome], 'Descrição': [desc], 
                           'Custo Produto': [ca], 'Custo Fixo/Administrativo': [cf], 
                           'Comissão Vendas': [cv], 'Imposto Produto': [iv], 
                           'Rentabilidade': [ml]})

nova_linha.to_csv('dados.csv', mode='a', header=False, index=False)

print("Nova linha adicionada com sucesso ao arquivo dados.csv.")

dados

#cálculo pv

PV= ca/1-((cf+cv+iv+ml)/100)