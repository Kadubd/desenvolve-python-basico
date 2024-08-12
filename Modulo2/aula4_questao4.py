valor = int(input("Digite um valor" ))#lê o valor digitado
nota100 = valor // 100#calcula a quantidade de cédulas de 100
valor = valor % 100 #atualiza a variavel valor após a operação
nota50 = valor // 50 #calcula a quantidade de cédulas de 50
valor = valor % 50#atualiza o a variavel valor após a operação
nota20 = valor // 20 #calcula a quantidade de cédulas de 20
valor = valor % 20#atualiza o a variavel valor após a operação
nota10 = valor // 10 #calcula a quantidade de cédulas de 10
valor = valor % 10#atualiza o a variavel valor após a operação
nota5 = valor // 5 #calcula a quantidade de cédulas de 5
valor = valor % 5#atualiza o a variavel valor após a operação
nota1 = valor // 1 #calcula a quantidade de cédulas de 1
print("Em cedulas seria...")
print(f"{nota100} nota(s) de R$100,00")
print(f"{nota50} nota(s) de R$50,00")
print(f"{nota20} nota(s) de R$20,00")
print(f"{nota10} nota(s) de R$10,00")
print(f"{nota5} nota(s) de R$5,00")
print(f"{nota1} nota(s) de R$1,00")