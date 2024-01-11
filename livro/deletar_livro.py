from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro


def deletarLivro(id: int):
    livro = buscarLivro(id)
    if livro:
        livros.remove(livro)
        print('Livro removido com sucesso!')
    else:
        print('Erro: Livro não encontrado!!')


if __name__ == "__main__":
    print(livros)
    deletarLivro(1)
    print(livros)
    deletarLivro(1)