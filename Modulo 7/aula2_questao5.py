import random
def embaralhar_palavras(frase):
    # Função auxiliar para embaralhar as letras internas de uma palavra
    def embaralhar_palavra(palavra):
        # Se a palavra tiver 3 letras ou menos, não precisa embaralhar
        if len(palavra) <= 3:
            return palavra  
        # Separa a primeira e a última letra, e embaralha as letras do meio
        meio = list(palavra[1:-1])  # Letras internas
        random.shuffle(meio)  # Embaralha as letras do meio 
        # Reconstrói a palavra com a primeira letra, letras embaralhadas e última letra
        return palavra[0] + ''.join(meio) + palavra[-1]
    # Divide a frase em palavras, embaralha cada uma, e junta novamente
    palavras = frase.split()  # Divide a frase em palavras
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras] 
    return ' '.join(palavras_embaralhadas)
# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
