import gato, cachorro, coelho
import mysql.connector
conexao= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cad_bd'
)
gato = gato.Gato("Bichano", "Branco","12")
cachorro = cachorro.Cachorro("Totó", "Preto",12)
coelho = coelho.Coelho("Pernalonga", "Cinza",12)

gato.comer()
cachorro.comer()
coelho.comer()
