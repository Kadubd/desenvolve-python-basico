ln = []
lnpar = []
lnimpar = []
for i in range(5): #repete 5 vezes
    a = int(input("Digite um número inteiro... ")) #solicita um valor inteiro
    ln.append(a) #adiciona esse valor à lista 
for elem in ln: #Lê cada elemento da lista
    if elem%2 ==0: #se o elemnto lido for par(ou seja o resto da divisão desse número por 2 for igual a 0)
        lnpar.append(elem) #adiciona-se esse elemento à lista contendo os valores pares
    else: #se nãoo for
        lnimpar.append(elem) #adiciona-se esse elemento à lista contendo os valores ímpares
print(ln) #imprime a lista original
print(f"Os 3 primeiros elementos da lista são: {ln[0:3]}") #imprime os 3 primeiros elementos da lista
print(f"Lista invertida: {ln[::-1]}") #imprime a lista invertida
print(f"Os elementos pares da lista são: {lnpar}") #imprime os elementos pares da lista
print(f"Os elementos ímpares da lista são: {lnimpar}") #imprime os elementos ímpares da lista