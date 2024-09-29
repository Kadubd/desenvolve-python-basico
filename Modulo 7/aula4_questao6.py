import csv

# Função para verificar se a linha é válida
def linha_valida(linha):
    # Verifica se há mais de um artista ou se há caracteres especiais
    if linha['artist_count'] > '1' or '"' in linha['track_name']:
        return False
    return True

# Dicionário para armazenar a música mais tocada de cada ano
musicas_por_ano = {}

# Abre o arquivo para leitura
with open('spotify-2023.csv', encoding='latin-1') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    # Processa cada linha do arquivo
    for linha in leitor_csv:
        ano = int(linha['released_year'])
        # Verifica se o ano está no intervalo de 2012 a 2022
        if 2012 <= ano <= 2022:
            # Verifica se a linha é válida
            if linha_valida(linha):
                # Converte o número de streams para um inteiro
                streams = int(linha['streams'])
                # Se o ano não estiver no dicionário ou a música atual tiver mais streams, atualiza
                if ano not in musicas_por_ano or streams > musicas_por_ano[ano][3]:
                    musicas_por_ano[ano] = [linha['track_name'], linha['artist(s)_name'], ano, streams]

# Cria a lista com as músicas mais tocadas de cada ano
resultado = [[info[0], info[1], info[2], info[3]] for info in musicas_por_ano.values()]

# Imprime a lista resultante
print(resultado)
