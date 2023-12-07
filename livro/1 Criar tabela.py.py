import mysql.connector


meubanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"

)

print(meubanco)


meucursor = meubanco.cursor()

sql = "CREATE TABLE livros (Livro VARCHAR(50)NOT NULL, Autor VARCHAR(50)NOT NULL, ISBN VARCHAR(50)NOT NULL)"
meucursor.execute(sql)
print("Tabela criada com sucesso!!!")

meubanco.commit()