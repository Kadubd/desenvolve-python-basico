import os
frase = input("Digite uma frase: ")
nome_arquivo = "frase.txt"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)
caminho_completo = os.path.abspath(nome_arquivo)
print(f"Arquivo salvo em: {caminho_completo}")