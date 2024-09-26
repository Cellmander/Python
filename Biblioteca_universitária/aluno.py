from usuario_bu import UsuarioBU
from abc import abstractmethod, ABC

class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def emprestar(self, titulo_livro):
        return 'Aluno de matricula ' + '"' + str(self.__matricula) + '"' + super().emprestar(titulo_livro)
    
    def devolver(self, titulo_livro):
        return 'Aluno de matricula ' + '"' + str(self.__matricula) + '"' + super().devolver(titulo_livro)