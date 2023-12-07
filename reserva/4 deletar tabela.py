import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"
)
print(meubanco)

meucursor = meubanco.cursor()

try:
    meucursor.execute("DROP TABLE reserva")
    print("Tabela excluída com Sucesso!!!")

except:
    print("Tabela não removida. Reveja os comandos usados")