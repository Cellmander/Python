from usuario_bu import UsuarioBU
from abc import abstractmethod, ABC

class Funcionario(UsuarioBU, ABC):

    @abstractmethod
    def __init__(self, departamento, cpf, dias_de_emprestimo):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def emprestar(self, titulo_livro):
        return 'do departamento ' + '"' + self.__departamento + '"' +  super().emprestar(titulo_livro)
    
    def devolver(self, titulo_livro):
        return 'do departamento ' '"' + self.__departamento + '"' + super().devolver(titulo_livro)