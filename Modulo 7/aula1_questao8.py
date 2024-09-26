def calcular_primeiro_digito(cpf):
    # Extrai os primeiros 9 dígitos do CPF
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
    # Verifica se o CPF tem ao menos 9 dígitos
    if len(cpf_numeros) < 9:
        return None
    # Multiplicamos cada dígito da direita para a esquerda por números crescentes a partir de 2
    soma = 0
    for i, peso in zip(cpf_numeros[:9], range(10, 1, -1)):
        soma += i * peso
    # Calcula o primeiro dígito verificador
    resto = (soma * 10) % 11
    primeiro_digito = 0 if resto == 10 or resto == 11 else resto
    return primeiro_digito
def validar_cpf(cpf):
    # Remove os caracteres não numéricos (pontos e traços)
    cpf_limpo = ''.join([char for char in cpf if char.isdigit()])
    # Verifica se o CPF tem 11 dígitos
    if len(cpf_limpo) != 11:
        return "Inválido"   
    # Calcula o primeiro dígito verificador
    primeiro_digito = calcular_primeiro_digito(cpf)   
    # Verifica se o primeiro dígito bate com o esperado
    if primeiro_digito == int(cpf_limpo[9]):
        return "Válido"
    else:
        return "Inválido"
# Solicita o CPF do usuário
cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
# Valida o CPF
resultado = validar_cpf(cpf_usuario)
print(f"CPF {resultado}")