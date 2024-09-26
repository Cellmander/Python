from funcionario import Funcionario

class Administrativo(Funcionario):

    def __init__(self, cpf, departamento):
        super().__init__(cpf, departamento, dias_de_emprestimo=10)
    
    def emprestar(self, titulo_livro):
        return 'Funcionario administrativo ' + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro):
        return 'Funcionario administrativo ' + super().devolver(titulo_livro)