from livro.livro_repositorio import livros

def listarLivros():
    print('--- Lista de livros ---')
    for livro in livros:
        print(f"Id: {livro['id']}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Editora: {livro['editora']}")
        print(f"Disponível: {livro['disponivel']}")
        print("*"*50)

if __name__ == "__main__":
    listarLivros()