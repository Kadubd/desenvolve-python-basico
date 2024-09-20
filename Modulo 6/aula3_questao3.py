import random
li = [random.randint(-10, 10) for _ in range(20)] #gera 20 números entre -10 e 10
def emin(li): #função que descobre qual o intervalo com a maior quantidade de números negativos
    for i in range(len(li)): #Lê cada elemento da lista e encontra qual o intervado com a maior quantidade de números negativos
        for j in range(i+1, len(li)+1): 
            sublista = li[i:j]
            cn = sum(1 for num in sublista if num < 0)
            if cn > maxn:
                maxn = cn
                ini = i
                inf = j
    return ini, inf
print(f"Lista original: {li}") #Imprime a lista original
inicio, fim = emin(li) #deleta o intervalo
del li[inicio:fim]
print(f"Lista após deletar o intervalo com mais negativos: {li}") #imprime a lista com as alterações feitas