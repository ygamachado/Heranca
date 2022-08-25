import animal
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cad_bd"
)
conexao.cursor()


class Passaro(animal.Animal):
    def __init__(self, nome, cor, idade):
        super().__init__(nome, cor, idade)
x=5
print('ola mundo')
while(x>3):
    print("ola mundo")