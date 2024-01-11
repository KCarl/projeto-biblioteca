from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def editarLivro(id: int, titulo: str, editora: str, disponivel: bool):
    livro = buscarLivro(id)
    if livro:
        livro['titulo'] = titulo
        livro['editora'] = editora
        livro['disponivel'] = disponivel
        print('Dados alterados com sucesso!')
        return
    print('Erro: Livro não encontrado!')

if __name__ == "__main__":
    editarLivro(1, "Harry potter III", "infinity", False)
    print(livros)