# Lista de livros com suas informações
livros = [
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["1984", "George Orwell", 1949, 328],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["Dom Casmurro", "Machado de Assis", 1899, 288],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 432],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 552],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["A Catcher in the Rye", "J.D. Salinger", 1951, 277],
    ["O Alquimista", "Paulo Coelho", 1988, 208]
]

# Cria o arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escreve os títulos das colunas
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve as informações dos livros
    for livro in livros:
        arquivo.write(",".join(map(str, livro)) + "\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")
