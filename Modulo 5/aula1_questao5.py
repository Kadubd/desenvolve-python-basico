emojis = {
    ":smile:": "😊",
    ":heart:": "❤️",
    ":thumbsup:": "👍",
    ":sun:": "☀️",     #lista de emojis
    ":star:": "⭐",
    ":coffee:": "☕",
    ":clap:": "👏",
    ":fire:": "🔥"
}
print("Lista de emojis disponíveis:") #imprime a lista de emojis
for texto, emoji in emojis.items():
    print(f"{texto} -> {emoji}")
frase_codi = input("\nDigite uma frase codificada usando os códigos de emojis acima: ") #Lê a frase codificada
frase_deco = frase_codi 
for texto, emoji in emojis.items(): #começa a decodificar a frase
    frase_deco = frase_deco.replace(texto, emoji) #decodifica
print(f"Frase decodificada: {frase_deco}")