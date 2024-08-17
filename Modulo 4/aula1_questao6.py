exp = int(input("Quantos experimentos foram realizados este ano ? ")) #Lê a quantidade de experimentos
s = 0
r = 0
c = 0
total = 0
while exp>0:
    x = str(input("Qual animal foi usado como cobaia ? ")) #Lê o animal usado no experimento
    y = int(input("Quantos foram utilizados ? "))
    if x == "Coelho" or x == "coelho":
        c = c + y
    elif x == "Sapo" or x == "sapo":
        s = s + y
    elif x == "Rato" or x == "rato":
        r = r + y
    total = total + y
    exp = exp - 1
rpor = r/total
print(rpor)
print(f"Total de cobaias é de {total}")
print(f"O total de ratos é de {r}")
print(f"O total de coelhos é de {c}")
print(f"O total de sapos é de {s}")