import re
with open("estomago.txt", "r") as arquivo:
    linhas = arquivo.readlines()
print("Primeiras 25 linhas do arquivo:")
for i in range(min(25, len(linhas))):
    print(linhas[i].strip())
numero_de_linhas = len(linhas)
print(f"\nNúmero total de linhas: {numero_de_linhas}")
linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres:\n{linha_maior.strip()}")
contagem_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
contagem_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))
total_mencoes = contagem_nonato + contagem_iria
print(f"\nNúmero de menções a 'Nonato' e 'Íria': {total_mencoes}")