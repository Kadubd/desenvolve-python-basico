#lê o nome do produto 1
nomeitem1 = str(input("_Qual o nome do item?_"))
#lê o valor do produto 1
valoruni1 = float(input("_Qual o valor do item?_"))
#lê a quantidade do produto 1
qua1 = int(input("_Qual a quantidade?_"))
#lê o nome do produto 2
nomeitem2 = str(input("Qual o nome do item?"))
#lê o valor do produto 2
valoruni2 = float(input("Qual o valor do item?"))
#lê a quantidade do produto 2
qua2 = int(input("Qual a quantidade?"))
#lê o nome do produto 3
nomeitem3 = str(input("Qual o nome do item?"))
#lê o valor do produto 3
valoruni3 = float(input("Qual o valor do item?"))
#lê a quantidade do produto 3
qua3 = int(input("Qual a quantidade?"))
valortotal1 = valoruni1*qua1
valortotal2 = valoruni2*qua2
valortotal3 = valoruni3*qua3
valortotal = valortotal1+valortotal2+valortotal3
print(f"Total:R${valortotal:,.2f}")
