import random 
n = [random.randint(-100, 100) for i in range(20)] #gera 20 valores aleatorios entre -100 e 100 e armazena eles na lista "n0"
mini=min(n) #descobre qual o menor valor da lista
minindex= n.index(mini) #descobre qual o indice desse valor
maxi = max(n) #descobre qual o maior valor da lista
maxindex = n.index(maxi) #descobre qual o indice desse valor
print(f"lista: {n}") #imprime a lista
print(f"lista em ordem: {sorted(n)}") #imprime a lista em ordem crescente
print(f"lista original: {n}") #Imprime a lista original
print(f"índice do maior valor da lista: {maxindex}") #imprime o indice do maior valor da lista
print(f"índice do menor valor da lista: {minindex}") #imprime o indice do menor valor da lista