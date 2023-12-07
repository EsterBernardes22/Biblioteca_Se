import mysql.connector


meubanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"

)

print(meubanco)

meucursor = meubanco.cursor()


sql = "CREATE TABLE reserva (Professor VARCHAR(50)NOT NULL, Turma VARCHAR(50)NOT NULL, Turno VARCHAR(50)NOT NULL, Mês VARCHAR(50)NOT NULL, Data INT DEFAULT 0, PRIMARY KEY(Professor))"
meucursor.execute(sql)
print("Tabela criada com sucesso!!!")

meubanco.commit()