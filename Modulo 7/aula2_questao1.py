def converter_data_nascimento(data_str):
    # Lista com os meses por extenso
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']   
    # Separa a string de entrada em dia, mês e ano
    dia, mes, ano = data_str.split('/') 
    # O índice da lista é o mês - 1, já que a lista começa do índice 0
    mes_extenso = meses[int(mes) - 1]
    # Retorna a data no formato: dd de mês por extenso de aaaa
    return f'{int(dia)} de {mes_extenso} de {ano}'
# Solicita a data de nascimento do usuário
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
# Exibe a data com o mês por extenso
print(converter_data_nascimento(data_nascimento))