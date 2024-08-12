#lê o comprimento
compri = int(input("Qual o comprimento do terreno?"))
#lê a largura
larg = int(input("Qual a largura do terreno?"))
#lê o valor do metro quadrado
valor = float(input("Qual o valor do metro quadrado na região?"))
#calcula quantos m2 o terreno tem
area = compri*larg
#calcula o valor do terreno
preco = area*valor
#diz o tamanho e valor do terreno
print(f"O terreno possui {area}m2 e custa R${preco:,.2f}")