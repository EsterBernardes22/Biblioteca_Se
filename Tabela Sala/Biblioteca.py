from bs4 import BeautifulSoup
import requests
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"
)
cursor = conexao.cursor()

class Sala:
    def __init__(self, lugar, bloco, capacidade, estrutura):
        self.lugar = lugar
        self.bloco = bloco
        self.capacidade = capacidade
        self.estrutura = estrutura

    def __str__(self):
        return f"Sala {self.lugar}, Bloco {self.bloco}, Capacidade {self.capacidade}, Estrutura {self.estrutura}"

salas = []

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Salas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        lugar VARCHAR(255),
        bloco VARCHAR(255),
        capacidade INT,
        estrutura VARCHAR(255)
    )
""") 

def extrair_e_adicionar():
    url = "http://127.0.0.1:5500/Biblioteca%20Senai/bibliotecavirtual.html"
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        if not table:
            print("Nenhuma tabela encontrada na página HTML.")
            return

        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            lugar, bloco, capacidade, estrutura = [col.text.strip() for col in columns]
            adicionar_sala(lugar, bloco, capacidade, estrutura)

        print("Dados extraídos e adicionados com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página HTML: {e}")

def adicionar_sala(lugar, bloco, capacidade, estrutura):
    cursor.execute("""
        INSERT INTO Salas (lugar, bloco, capacidade, estrutura)
        VALUES (%s, %s, %s, %s)
    """, (lugar, bloco, capacidade, estrutura))
    conexao.commit()
    salas.append(Sala(lugar, bloco, capacidade, estrutura))

extrair_e_adicionar()

for sala in salas:
    print(sala)

try:
    conexao.close()
except mysql.connector.Error as err:
    print(f"Erro ao fechar a conexão: {err}")
finally:
    print("Conexão fechada.")
