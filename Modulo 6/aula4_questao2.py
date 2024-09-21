frase = str(input("Escreva uma frase... "))
vogais = [l for l in frase.lower if l in 'aeiou'] #Verifica se os as letras da frase estão entre as vogais se estiverem elas são adicionadas à lista  
consoantes = [l for l in frase.lower if l not in 'aeiou '] #Faz a mesma coisa só que dessa vez descobrindo as consoates
vogais_ord = sorted(vogais) #coloca as vogais em ordem alfabetica
print(f"Sua fraze é '{frase}'")
print(f"As vogais da frase são: {vogais_ord}")
print(f"As consoates são: {consoantes}")