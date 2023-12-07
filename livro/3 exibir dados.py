import mysql.connector


meubanco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senai125@",
    database = "biblioteca"
)

print(meubanco)

try:
    meucursor = meubanco.cursor()
    sql = "Select * from livros"
    meucursor.execute(sql)

    resultados = meucursor.fetchall()
    primeiro = resultados [0] if len(resultados) else None
    print(resultados)
except:
    print("Encontramos alguns erros!")

for registros in resultados:
    print(registros)