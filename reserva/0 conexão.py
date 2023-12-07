import mysql.connector


meubanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@"

)

print(meubanco)

