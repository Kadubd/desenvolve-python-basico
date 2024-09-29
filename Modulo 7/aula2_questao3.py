import string

# Função para verificar se uma frase é palíndromo
def eh_palindromo(frase):
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum()) # Remove espaços, pontuação e coloca tudo em minúsculas
    return frase_limpa == frase_limpa[::-1] # Verifica se a frase limpa é igual ao seu reverso
# Loop principal do programa
while True:
    frase = input("Digite uma frase (ou 'Fim' para encerrar): ") # Solicita a frase do usuário
    if frase.lower() == "fim":
        print("Programa encerrado.")  # Verifica se o usuário quer encerrar o programa
        break
    if eh_palindromo(frase):
        print("É um palíndromo!")     # Verifica se a frase é um palíndromo
    else:
        print("Não é um palíndromo.")
