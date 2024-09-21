alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60] #Lê o nome do aluno e sua nota se a nota for maior ou igual a 60 se adiciona o nome a essa lista
print(f"aprovado(s): {aprovados}")