import animal

class Coelho(animal.Animal):
    def __init__(self, nome, cor, idade):
        super().__init__(nome, cor, idade)