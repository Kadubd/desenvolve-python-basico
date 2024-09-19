import random
a1 = (random.randint(0, 10)) #gera um valor aleatorio entre 1 e 10
a2 = (random.randint(0, 10)) #gera um valor aleatorio entre 1 e 10
l1 = [random.randint(0, 10) for i in range(a1)] #gera a uma quantidade aleatoria entre 1 a 10 de números de 1 a 10
l2 = [random.randint(0, 10) for i in range(a2)] #gera a uma quantidade aleatoria entre 1 a 10 de números de 1 a 10
interc = [] #cria a lista "interc" que vai conter a interseção
minl = min(len(l1), len(l2)) #descobre qual a menor lista
for i in range(minl): #vai repetir a mesma quantidade de vezes que correspondem a quantidade de valores que a menor lista contem
    interc.append(l1[i]) #vai adicionar um elemento da lista 1 à interc
    interc.append(l2[i]) #vai adicionar um elemento da lista 2 à interc
if len(l1) > len(l2): #se a lista 1 for maior que a lista dois
    interc.extend(l1[minl:]) #vai ser adicionando ao final os elementos remanescentes da lista 1
else: #se não
    interc.extend(l2[minl:]) #vai ser adicionando ao final os elementos remanescentes da lista 2
print(f"Lista 1: {l1}") #imprime a lista 1
print(f"Lista 2: {l2}") #imprime a lista 2
print(f"interseção: {interc}") #imprime a lista interc