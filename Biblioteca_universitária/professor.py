from funcionario import Funcionario

class Professor(Funcionario):

    def __init__(self, cpf, departamento):
        super().__init__(cpf, departamento, dias_de_emprestimo=20)

    def emprestar(self, titulo_livro):
        return 'Professor ' + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro):
        return 'Professor ' + super().devolver(titulo_livro)
