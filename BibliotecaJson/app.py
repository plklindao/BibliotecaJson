# Arquivo principal do sistema

from models.livro import Livro
from services.biblioteca_service import carregar_livros, salvar_livros

livros = carregar_livros()

print("==================================")
print("===== SISTEMA DE BIBLIOTECA ======")
print("==================================")

print("Categoria padrão: ", Livro.categoria_padrao())

while True:
    print("\nMENU")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Alterar título")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar livro
    if opcao == "1":
        print("\nCadastro de Livro")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano de publicação: "))

        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        salvar_livros(livros)
        print("Livro cadastrado!")

    # Listar livros
    elif opcao == "2":
        print("\n Lista de Livros")
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for i, livro in enumerate(livros):
                print("Livro", i)
                livro.exibir()

    # Alterar título do livro
    elif opcao == "3":
        for i, livro in enumerate(livros):
            print(i, ' - ', livro.titulo)
            
        pos = int(input("Escolha o número do livro: "))
        novo = input("Novo título: ")
        livros[pos].titulo = novo
        salvar_livros(livros)
        print("Título alterado!")

    # Sair do sistema
    elif opcao == "4":
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida.")
