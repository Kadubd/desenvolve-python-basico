dist = int(input("Digite a distância para onde deseja enviar o produto em km... "))
peso = int(input("Digite o peso do item que deseja enviar em kg... "))
if dist<=100:
    valorpeso = 1
if dist>100 and dist<=300:
    valorpeso = 1.5
if dist>300:
    valorpeso = 2
valorfrete = valorpeso*peso
if peso>10:
    valorfrete = valorfrete+10
print(f"o valor da entrega será de R${valorfrete:,.2f}")
