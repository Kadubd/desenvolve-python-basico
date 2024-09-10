import random
aleatorio = (random.randint(0, 10)) #gera um número aleatorio entre 1 e 10
while True: #Enquanto o comando "break" não ocorrer vai se repetir
    n = int(input("Adivinhe o número entre 1 e 10! ")) #Solicita um número
    if n==aleatorio: break #se o numero digitado for igual ao numero aleatorio o comando break é ativado
    if n > aleatorio: #se o numero for menor que o número aleatorio
        print("Muito alto, tente novamente! ") #Imprime-se
    if n < aleatorio: #se o numero for menor que o número aleatorio
        print("Muito baixo, tente novamente! ") #Imprime-se
print(f"Parabens você acertou!! O número era o {aleatorio}") #imprime o número certo e que você acertou
