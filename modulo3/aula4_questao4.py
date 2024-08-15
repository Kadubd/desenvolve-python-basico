dist = int(input("Digite a distância para onde deseja enviar o produto em km... ")) #Lê o distância
peso = int(input("Digite o peso do item que deseja enviar em kg... ")) #Lê o peso
if dist<=100: #calcula o valor apartir da distancia de até 100km
    valorpeso = 1 
if dist>100 and dist<=300: #calcula o valor apartir da distancia de 101km a 300km
    valorpeso = 1.5
if dist>300:
    valorpeso = 2
valorfrete = valorpeso*peso #calcula o valor para distancias acima de 300km
if peso>10: #calcula o peso, caso o peso for acima e 10kg um acrescimo de 10 reais será adicionado ao valor da entrega
    valorfrete = valorfrete+10 #calcula o valor da entrega
print(f"o valor da entrega será de R${valorfrete:,.2f}") #imprime o valor 
