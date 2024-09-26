def encontrar_anagramas(string, objetivo):
    # Tamanho da palavra objetivo
    tamanho_objetivo = len(objetivo)
    # Ordena a palavra objetivo para facilitar a comparação
    objetivo_ordenado = sorted(objetivo)
    # Lista para armazenar os anagramas encontrados
    anagramas = []
    # Percorre a string original
    for i in range(len(string) - tamanho_objetivo + 1):
        # Extrai uma subsequência de tamanho equivalente à palavra objetivo
        subsequencia = string[i:i + tamanho_objetivo]
        # Verifica se a subsequência é um anagrama
        if sorted(subsequencia) == objetivo_ordenado:
            anagramas.append(subsequencia)
    return anagramas
# Solicita a string e a palavra objetivo do usuário
string = input("Digite a string: ")
objetivo = input("Digite a palavra objetivo: ")
# Chama a função e exibe os anagramas encontrados
anagramas_encontrados = encontrar_anagramas(string, objetivo)
print(f"Anagramas de '{objetivo}' encontrados: {anagramas_encontrados}")