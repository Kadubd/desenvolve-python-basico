import random
def encrypt(strings):
    # Gera um valor de chave aleatório entre 1 e 10
    chave = random.randint(1, 10)
    # Função auxiliar para criptografar um único caracter
    def criptografar_caractere(caracter, chave):
        unicode_min = 33  # Limite inferior do intervalo visível
        unicode_max = 126 # Limite superior do intervalo visível 
        # Pega o código Unicode do caractere
        codigo = ord(caracter) 
        # Verifica se o caractere está dentro do intervalo de caracteres visíveis
        if unicode_min <= codigo <= unicode_max:
            # Calcula o novo código com o deslocamento circular
            novo_codigo = codigo + chave
            
            # Caso o código ultrapasse o limite, volta ao início do intervalo
            if novo_codigo > unicode_max:
                novo_codigo = unicode_min + (novo_codigo - unicode_max - 1)
                
            # Retorna o novo caractere criptografado
            return chr(novo_codigo)
        else:
            # Retorna o caractere original se estiver fora do intervalo
            return caracter
    # Lista para armazenar as strings criptografadas
    criptografados = []
    # Criptografa cada string da lista
    for string in strings:
        # Aplica a criptografia a cada caractere da string
        string_criptografada = ''.join(criptografar_caractere(c, chave) for c in string)
        criptografados.append(string_criptografada)
    # Retorna a lista de strings criptografadas e a chave usada
    return criptografados, chave
# Exemplo de uso
nomes = ["Alice", "Bob", "Carlos"]
cripto_nomes, chave_cripto = encrypt(nomes)
print(f"Nomes criptografados: {cripto_nomes}")
print(f"Chave de criptografia: {chave_cripto}")
