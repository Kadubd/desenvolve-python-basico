classe = str(input("Qual a classe do seu personagem? "))
Forca = int(input("Digite os pontos de força (de 1 a 20): "))
Magia = int(input("Digite os pontos de magia (de 1 a 20): "))
classeM = classe=="mago" or classe=="Mago"
ForcaM = Forca>10 or Forca==10
MagiaM = Magia>15 or Magia==15
Mago1 =not MagiaM!=ForcaM
Mago = not Mago1!=classeM
print(ForcaM, MagiaM, classeM)
classeG = classe=="Guerreiro" or classe=="guerreiro"
ForcaG = Forca>15 or Forca==15
MagiaG = Magia>10 or Magia==10
Guerreiro = MagiaG==ForcaG and classeG==ForcaG
classeA = classe=="Arqueiro" or classe=="arqueiro"
ForcaA = Forca>5 or Forca==5 and Forca<15 or Forca==15
MagiaA = Magia>5 or Magia==5 and Magia<15 or Magia==15
arqueiro = MagiaA==ForcaA and classeA==ForcaA
consitente = arqueiro!=Guerreiro or Guerreiro!=Mago
print(f"Pontos de atributo consistentes com a classe escolhida: {consitente}")