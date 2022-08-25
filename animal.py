class Animal():
    def __init__(self, nome, cor, idade):
        self.__nome = nome
        self.__cor = cor
        self.__idade = idade

    def comer(self):
        print(f"O {self.__nome} cor {self.__cor} idade {self.__idade} está comendo")
