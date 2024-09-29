import random

# Função para imprimir o estado do enforcado
def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r") as f:
        enforcados = f.read().splitlines()
        print(enforcados[erros])

# Função principal do jogo da forca
def jogar():
    # Lê as palavras do arquivo gabarito_forca.txt
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()

    # Escolhe uma palavra aleatória
    palavra = random.choice(palavras).upper()
    letras_adivinhadas = []
    erros = 0
    tentativas_maximas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")

    # Loop principal do jogo
    while erros < tentativas_maximas:
        # Mostra o progresso do jogador
        progresso = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(f"\nProgresso: {progresso}")

        # Verifica se o jogador já adivinhou a palavra
        if '_' not in progresso:
            print("Parabéns! Você adivinhou a palavra!")
            break

        # Permite que o jogador adivinhe uma letra
        letra = input("Digite uma letra: ").upper()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.append(letra)

        # Verifica se a letra está na palavra
        if letra not in palavra:
            erros += 1
            print(f"Lamento, a letra '{letra}' não está na palavra.")
            imprime_enforcado(erros)

    if erros == tentativas_maximas:
        print(f"Você perdeu! A palavra era: {palavra}")

# Inicia o jogo
if __name__ == "__main__":
    jogar()
