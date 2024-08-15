idade = int(input("Qual sua idade?") )#lê a idade inserida
jogou = int(input("Quantos jogos de Tabuleiro você já jogou?") ) #lê quantos jogos de tabuleiro a pessoa jogou
venceu = int(input("Quantos jogos você já venceu?") )#lê quantos jogos de tabuleiro ele venceu
idadene = idade<=18 and idade>=16 #calcula se a idade inserida por volta de 16 a 18 anos
jogoune = jogou>3 or jogou==3 #calcula se a pessoa já jogou pelo menos três jogos
venceune = venceu>1 or venceu==1 #calcula se a pessoa já venceu pelo menos 1 jogo
perm1 = venceune==idadene and idadene==jogoune #descobre se todos são true
print(f"Apto para ingressar no clube de jogos de tabuleiro:{perm1}") 