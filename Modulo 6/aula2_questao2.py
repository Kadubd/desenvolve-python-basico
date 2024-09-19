import random
num_elementos = (random.randint(5, 20) for i in range(1))
elementos = [random.randint(1, 10) for i in range(num_elementos)]
print(f"lista: {elementos}")
print(f"Soma dos valores da lista: {sum(elementos)}")
print(f"Média dos valores da lista: {sum(elementos)/len(elementos)}")