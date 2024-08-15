classe = str(input("Qual a classe do seu personagem? "))
Forca = int(input("Digite os pontos de força (de 1 a 20): "))
Magia = int(input("Digite os pontos de magia (de 1 a 20): "))
classeM = classe=="mago" or classe=="Mago" #confirma a classe
ForcaM = Forca>10 or Forca==10 #verifica se o personagem tem a força necessária
MagiaM = Magia>15 or Magia==15 #verifica se o personagem tem a magia necessária
Mago1 =not MagiaM!=ForcaM #verifica se o personagem está consistente
Mago = not Mago1!=classeM
classeG = classe=="Guerreiro" or classe=="guerreiro" #confirma a classe
ForcaG = Forca>15 or Forca==15 #verifica se o personagem tem a força necessária
MagiaG = Magia>10 or Magia==10 #verifica se o personagem tem a magia necessária
Guerreiro = MagiaG==ForcaG and classeG==ForcaG #verifica se o personagem está consistente
classeA = classe=="Arqueiro" or classe=="arqueiro" #confirma a classe
ForcaA = Forca>5 or Forca==5 and Forca<15 or Forca==15 #verifica se o personagem tem a força necessária
MagiaA = Magia>5 or Magia==5 and Magia<15 or Magia==15 #verifica se o personagem tem a magia necessária
arqueiro = MagiaA==ForcaA and classeA==ForcaA #verifica se o personagem está consistente
consitente = arqueiro!=Guerreiro or Guerreiro!=Mago #confirma se o personagem está consistente dentre as classes
print(f"Pontos de atributo consistentes com a classe escolhida: {consitente}") #imprime o resultado 