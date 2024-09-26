frase = input("Digite uma frase... ")
indice = []
vogais = 0
for i in frase:
    if i in "aeiou":
        indice.append(frase.index(i))
        vogais = vogais + 1
print(f"{vogais} Vogais")
print(f"Índices: {indice}")