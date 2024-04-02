#inserção de dados

import random
import pandas as pd

id = random.randint(1000, 9999)
nome = input("\nDigite o nome do produto: ")
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

print("\n-------//  Cálculo PV  //---------\n")

PV=cp/(1-((cf+cv+iv+ml)/100))
print(f"Descrição                   Valor  % ")
print(f"A.Preço de venda            {PV}   100%")
print(f"B.Custo de Aquisição        {cp}   {(cp*100)/PV}%")
print(f"C.Receita Bruta             {PV-cp}  {100-(cp*100)/PV}% ")
print(f"D.Custo fixo/Administrativo {PV*(cf/100)}  {cf}% ")
print(f"E.Comisão de vendas         {(cv/100)*PV}  {cv}% ")
print(f"F.Impostos                  {PV*(iv/100)}  {iv}% ")
print(f"G.Outros custos             {(PV*(cf/100))+((cv/100)*PV)+((iv/100)*PV)}  {cf+cv+iv}%")
print(f"H.Rentabilidade             {(PV-cp)-((PV*(cf/100))+((cv/100)*PV)+((iv/100)*PV))}  {ml}%\n")

lucroBruto = PV - cp
lucro = (lucroBruto / cp) * 100

if (lucro < 0):
    print("--- PREJUIZO ---\n")
elif(lucro == 0):
    print("--- EQUILÍBRIO ---\n")
elif((lucro > 0) and (lucro <= 10)):
    print("--- LUCRO BAIXO ---\n")
elif((lucro > 10) and (lucro <= 20)):
    print("--- LUCRO MÉDIO ---\n")
else:
    print("--- LUCRO ALTO ---\n")
print(f"O lucro do(a) {nome} é de {round(lucro, 2)}% (R${round(lucroBruto, 2)})\n")