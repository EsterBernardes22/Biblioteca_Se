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

sql = "INSERT INTO livros (Livro, Autor, ISBN) VALUES (%s, %s, %s)"
valores = [
    ("Amor e gelato", "WELCH, Jenna Evans","9788551002346"),
    ("Diário de um banana", "KINNEY, Jeff.","9788576831303"),
    ("Teto para dois", "O'LEARY, Beth", "9788551005415"),
    ("Vermelho, branco e sangue azul", "MCQUISTON, Casey", "9788555340949"),
    ("A seleção", "CASS, Kiera", "9788565765015"),
    ("O poder do hábito", "DUHIGG, Charles", "9788539004119"),
    ("A arte da guerra", "SUNZI","9788525426642"),
    ("Harry Potter e a pedra filosofal", "ROWLING, J. K","8532511015"),

]

try:
    meucursor.executemany(sql, valores)
    print(meucursor.rowcount, "registro(s) inserido(s)!")
except mysql.connector.Error as error:
    print("Ocorreu um erro ao inserir os registros:", error)

meubanco.commit()


