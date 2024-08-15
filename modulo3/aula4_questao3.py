ano = int(input("Digite um ano... ")) #Lê o ano
if ano%4==0 and ano%100!=0 or ano%400==0: #calcula se o ano e divisivel por 4 e não é dividido por 100 ou se ele é divisivel por 400
    print("Bissexto!") #imprime caso o ano seja bissexto
else: #Caso o ano não cumpra nenhum dos requisitos ele não é bissextpo
    print("Não Bissexto!!") #imprime que ele não é bissexto 
