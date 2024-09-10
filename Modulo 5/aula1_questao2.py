import random
import math
n = int(input("Digite a quantidade de números aleatórios (n): ")) #Lê o valor de n
valores = [random.randint(0, 100) for _ in range(n)] #Gera n números aleatorios
soma = sum(valores) #soma os números gerados na linha anterior
raiz_quadrada = math.sqrt(soma) #Calcula a raiz quadrada do resultado obtido da linha anterior
print(f"Os números gerados são: {valores}") #imprime os números aleatorios
print(f"A soma dos valores é: {soma}") #Imprime o valor da soma dos números
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}") #Imprive o valor da raiz
