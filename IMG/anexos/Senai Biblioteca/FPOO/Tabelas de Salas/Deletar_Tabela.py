import mysql.connector

# Conectar MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"
)
cursor = conexao.cursor()

# Visualizar Tabela
cursor.execute('SHOW TABLES')  
tabelas = cursor.fetchall()

print("Tabelas existentes:")
for tabela in tabelas:
    print(tabela[0])

# Deletar Tabela

nome_tabela = "salas"  

try:
    cursor.execute(f'DROP TABLE {nome_tabela}')
    print(f'Tabela {nome_tabela} excluída com sucesso!')

except mysql.connector.Error as err:
    print(f'Não foi possível excluir a tabela. Erro: {err}')

# Fechar MySQL
conexao.close()
