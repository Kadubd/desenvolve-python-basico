resp = int(input("Quantos respondentes tiveram ? ")) #Lê a quantidade de respondentes
M = resp #Lê o valor de "M"
idade = 0
while resp>0: #enquanto o número de respondentes for maior de 0
    quest = int(input("Qual a idade deste respondente ? ")) #Vai pedir e ler a idade deste respondente
    idade += quest #Vai adicionar esse valor a "idade"
    resp -= 1 #Vai diminuir 1 do valor total de "resp"
media = idade/M #Vai caulcular a média de idades
print(f"a média de idades é {media}") #Vai imprimir a média