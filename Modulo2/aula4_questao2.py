#lê o valor em fahrenheit
Fa = int(input("Digite o valor de fahrenheit"))
#calcula o valor em celsiu
celsium = (Fa-32)*(5/9)
#converte o valor para inteiro
C = int(celsium)
#diz o valor de ambos
print (f"{Fa} graus Fahrenheit são {C} graus Celsius.")