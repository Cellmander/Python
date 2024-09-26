from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.__autores.append(autor)
        self.__capitulos = []
        self.__capitulos.append(Capitulo(numero_capitulo, titulo_capitulo))

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if (isinstance(autor, Autor)) and (autor not in self.__autores):
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if not capitulo:
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if capitulo:
            self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo