from livro.livro_repositorio import livros

def buscarLivro(id: int) -> dict or None:
    for livro in livros:
        if livro['id'] == id:
            return livro
    return None


if __name__ == '__main__':
    print(buscarLivro(1))
    print(buscarLivro(2))