from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo, matricula)
    elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro):
        if self.__elaborando_tese:
           self.dias_de_emprestimo *= 2
        return super().emprestar(titulo_livro)
