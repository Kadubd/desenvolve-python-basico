tell  = input("Digite um número de celular... ")
if len(tell) == 8:
    tell = '9' + tell
elif len(tell) == 9:
    # Verifica se o primeiro dígito já é '9'
    if tell[0] != '9':
        print("O número já tem 9 dígitos, mas não começa com '9'.")
    else:
        print("O número já tem 9 dígitos e começa com '9'.")
else:
    print("Número inválido! Insira um número de celular com 8 ou 9 dígitos.")
# Adiciona o separador "-" e imprime o número formatado
if len(tell) == 9 and tell[0] == '9':
    numero_formatado = tell[:5] + '-' + tell[5:]
    print(f"Número formatado: {numero_formatado}")