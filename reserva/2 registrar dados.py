import mysql.connector

meubanco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Senai125@",
    database = "biblioteca"
)

print(meubanco)

meucursor = meubanco.cursor()

meucursor = meubanco.cursor()

sql = "INSERT INTO reserva (Professor, Turma, Turno, Mês, Data) VALUES (%s, %s, %s, %s, %s)"
valores = [
    ("Tom", "I2DSI","Manhã", "Dezembro", 7),
    ("Gleidsson", "I2DSI","Tarde", "Dezembro", 7),
    ("Max", "M2ADM", "Manhã", "Dezembro", 8),
    ("João", "I2ELE", "Tarde", "Dezembro", 8),
    ("Anderson", "M3MEC", "Manhã", "Dezembro", 11),
    ("Beth", "T2CAL", "Tarde", "Dezembro", 11),
    ("Cristiane", "M3F","Manhã", "Dezembro", 12),
    ("Jorge", "I2ELE","Manhã", "Dezembro", 14),
    ("Daniele", "T2ADM","Tarde", "Dezembro", 14),
    ("Miguel", "I2AUT","Manhã", "Dezembro", 15),
    ("Vitor", "I2AUT", "Tarde", "Dezembro", 15)

]

try:
    meucursor.executemany(sql, valores)
    print(meucursor.rowcount, "registro(s) inserido(s)!")
except mysql.connector.Error as error:
    print("Ocorreu um erro ao inserir os registros:", error)

meubanco.commit()


