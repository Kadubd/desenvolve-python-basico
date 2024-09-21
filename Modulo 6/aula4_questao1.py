li = []
li2 = [1,2,3,4,5,6,7,8,9]
li3 = []
li4 = []   
for i in range(0,30,3):     #gera as listas que serão retiradas os resultado
    li4.append(i)
for i in range(1,101):
    li3.append(i)
for i in range(20,51):
    li.append(i)
pares = [n for n in li if n%2==0] #cria uma lista onde se tem somente os valores pares de outra lista
quad = [n*n for n in li2] #cria uma lista onde se tem os quadrados dos vslores de outra lista
div7 = [n for n in li3 if n%7==0] #cria uma lista onde se contem os números divisiveis por 7 de outra lista
par_impar = ["par" if n%2==0 else "impar" for n in li4 ] #cria uma lista onde se tem escrito o que cada valor de outra lista é entre impar e par
print(f"Todos os números pares entre 20 e 50 são: {pares}")
print(f"O quadrado dos elementos da lista 2 são: {quad}")
print(f"Os números divisiveis por 7 entre 1 e 100 são: {div7}")
print(f"Entre par ou impar os elementos da lista 4 são respectivamente: {par_impar}")