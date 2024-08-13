gender = str(input("Qual seu gênero?(M ou F) "))
idade = int(input("Qual sua idade? "))
tempt = int(input("Quantos anos você já trabalhou? "))
genm = gender =="M" or gender =="m"
idadem = idade>=65
tempo = tempt>=30
ide = idade>=60 and tempt>=25
man = genm==idadem or tempo==genm or ide==genm
genf = gender=="F" or gender=="f"
idadef = idade>=60
fem = genf==idadef or tempo==genf or ide==genf
print(idadef)
print(tempo)
print(ide)
print(fem)