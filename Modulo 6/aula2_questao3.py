import random
l1 = [random.randint(0, 50) for i in range(20)]
l2 = [random.randint(0, 50) for i in range(20)]
interseccao = []
for valor in l1: #Lê cada valor da lista 1
    if valor in l2 and valor not in interseccao: #confere se o valor lido está na lista 2 e se ele não está em interseccao 
        interseccao.append(valor) #se for verdade adiciona esse valor a interseccao
def contar_ocorrencias(lista, valor): #função que descobre a quantidade de ocorrencias de um valor na lista interseccao
    return lista.count(valor) #retorna o valor descoberto
print("Lista 1:", l1) #imprime a lista 1
print("Lista 2:", l2) #imprime a lista 2
print(f"Interseção ordenada: {sorted(interseccao)}") #imprime a lista interseccao em ordem
for valor in interseccao: #Repete a quantidade de itens dentro da lista interseccao
    print(f"Valor {valor}: aparece {contar_ocorrencias(l1, valor)} vez(es) na Lista 1 e {contar_ocorrencias(l2, valor)} vez(es) na Lista 2") #imprime a quantidade de vezes cada valor da lista interseccao aparece nas duas listas
