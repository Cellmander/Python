class Pessoa: 
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

class Cargo:
    def __init__(self, salario, descricao):
        self.__salario = salario
        self.__descricao = descricao
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, cargo: Cargo):
        super().__init__(nome, cpf)
        if isinstance(cargo, Cargo):
            self.__cargo = cargo
        self.__dependentes = []