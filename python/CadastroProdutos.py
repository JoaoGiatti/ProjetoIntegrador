#inserção de dados

import random
import pandas as pd

print('''
================================================
            Cadastro de Produtos
================================================
''')

id = random.randint(1000, 9999)
nome = input("Digite o nome do produto: ")
desc = input("Digite a descrição do produto: ")
cp = float(input("Digite o custo do produto: "))
cf = float(input("Digite o custo fixo/administrativo: "))
cv = float(input("Digite o valor da comissão de vendas: "))
iv = float(input("Digite o valor do imposto sobre o produto: "))
ml = float(input("Digite o valor da rentabilidade: "))

#adicionando linha em 'dados.csv'

nova_linha = pd.DataFrame([[id, nome, desc, cp, cf, cv, iv, ml]],
                          columns=['ID', 'Nome', 'Descrição', 'Custo', 'Custo Fixo', 'Comissão Vendas', 'Imposto', 'Rentabilidade'])
nova_linha.to_csv("dados.csv")

print("Dados cadastrados!")

dados = pd.read_csv("dados.csv")

dados

#cálculo pv

print('''\n
================================================
         Cáculo Preço de Venda (PV)
================================================ 
\n''')

PV=(cp*((cf+cv+iv+ml)//100))+(cp/(1-(((cf+cv+iv+ml)%100)/100)))
print(f'''
Descrição ----------------- Valor - % 
A.Preço de venda            {round(PV,2)}   100%
B.Custo de Aquisição        {round(cp,2)}   {round(((cp*100)/PV),2)}%
C.Receita Bruta             {round((PV-cp),2)}  {round((100-(cp*100)/PV),2)}% 
D.Custo fixo/Administrativo {round((PV*(cf/100)),2)}  {cf}%
E.Comisão de vendas         {round(((cv/100)*PV),2)}  {cv}% 
F.Impostos                  {round(PV*(iv/100),2)}  {iv}% 
G.Outros custos             {round(((PV*(cf/100))+((cv/100)*PV)+((iv/100)*PV)),2)}  {cf+cv+iv}%
H.Rentabilidade             {round((PV-cp)-((PV*(cf/100))+((cv/100)*PV)+((iv/100)*PV)),2)}  {round(((100-(cp*100)/PV) -(cf+cv+iv)),2)}%\n
''')



if ((100-(cp*100)/PV) -(cf+cv+iv) < 0):
    print("------- PREJUIZO -------\n")
elif((100-(cp*100)/PV) -(cf+cv+iv) == 0):
    print("------- EQUILÍBRIO -------\n")
elif(((100-(cp*100)/PV) -(cf+cv+iv) > 0) and ((100-(cp*100)/PV) -(cf+cv+iv) <= 10)):
    print("------- LUCRO BAIXO -------\n")
elif(((100-(cp*100)/PV) -(cf+cv+iv) > 10) and ((100-(cp*100)/PV) -(cf+cv+iv) <= 20)):
    print("------- LUCRO MÉDIO -------\n")
else:
    print("------- LUCRO ALTO -------\n")
print(f"O lucro do(a) {nome} é de {round((100-(cp*100)/PV) -(cf+cv+iv), 2)}% (R${round((PV-cp)-((PV*(cf/100))+((cv/100)*PV)+((iv/100)*PV)),2)})\n")
