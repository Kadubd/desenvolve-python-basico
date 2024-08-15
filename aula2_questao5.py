gender = str(input("Qual seu gênero?(M ou F) ")) #lê o gênero
idade = int(input("Qual sua idade? ")) #lê a idade
tempt = int(input("Quantos anos você já trabalhou? ")) #lê o tempo trabalhado
genm = gender =="M" or gender =="m" #confirma o gênero
idadem = idade>=65 #verifica se a idade é o suficiente para aposentar
tempo = tempt>=30 #verifica se o tempo trabalhado é suficiente para aposentar
ide = idade>=60 and tempt>=25 #verifica se a pessoa tem tempo trabalhado e idade suficiente para aposentar
man = genm==idadem or tempo==genm or ide==genm #verifica se a pessoa pode aposentar
genf = gender=="F" or gender=="f" #confirma o gênero
idadef = idade>=60 #verifica se a idade é o suficiente para aposentar
fem = genf==idadef or tempo==genf or ide==genf #verifica se a pessoa pode aposentar
apto = fem!=man
print(f"Você está apto a se aposentar: {apto}")