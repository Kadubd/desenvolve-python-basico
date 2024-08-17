n1 = int(input("Digite um número... ")) #Lê o valor de n1
n2 = int(input("Digite um número... ")) #Lê o valor de n2
n3 = int(input("Digite um número... ")) #Lê o valor de n3
m = (n1+n2+n3)/3 #Calcula o valor de "m"
if m>=60: #Verifica se "m" é maior ou igual a 60 
    print("Aprovado!!") #se sim imprime "Aprovado"
elif m>=40: #Verifica se "m" é maior ou igual a 40
    print("Recuperação!!") #Se sim imprime "Recuperação"
else: #se nenhuma das anteriores forem verdade
    print("Reprovado!!") #imprime se "Reprovado"
print("Fim!") #finaliza o código