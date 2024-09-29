frase = input("Digite uma frase... ")
vogais = "aeiouAEIOU"
for i in vogais:
    frase = frase.replace(i, "*")
print(frase)