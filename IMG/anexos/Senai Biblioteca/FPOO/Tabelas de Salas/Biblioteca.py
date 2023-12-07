import tkinter as tk
from tkinter import messagebox
import pandas as pd
import mysql.connector

# Conectar MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senai125@",
    database="biblioteca"
)
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Salas (id INT AUTO_INCREMENT PRIMARY KEY,numero_sala INT,bloco VARCHAR(255),capacidade INT,estrutura VARCHAR(255))""")

conexao.commit()

class Sala:
    def __init__(self, numero_sala, bloco, capacidade, estrutura):
        self.numero_sala = numero_sala
        self.bloco = bloco
        self.capacidade = capacidade
        self.estrutura = estrutura

    def __str__(self):
        return f"Sala {self.numero_sala}, Bloco {self.bloco}, Capacidade {self.capacidade}, Estrutura {self.estrutura}"

# Função para adicionar sala à lista
def adicionar_sala(numero_sala, bloco, capacidade, estrutura):
    cursor.execute("""
        INSERT INTO Salas (numero_sala, bloco, capacidade, estrutura)
        VALUES (%s, %s, %s, %s)
    """, (numero_sala, bloco, capacidade, estrutura))
    conexao.commit()
    salas.append(Sala(numero_sala, bloco, capacidade, estrutura))
    messagebox.showinfo("Sucesso", "Sala adicionada com sucesso!")

# exibir as salas
def exibir_salas():
    info_salas = "\n".join(str(sala) for sala in salas)
    messagebox.showinfo("Salas", info_salas)

# Interface Gráfica
class Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Salas")
        self.geometry("400x200")

        self.label_numero = tk.Label(self, text="Número da Sala:")
        self.label_bloco = tk.Label(self, text="Bloco:")
        self.label_capacidade = tk.Label(self, text="Capacidade:")
        self.label_estrutura = tk.Label(self, text="Estrutura:")

        self.entry_numero = tk.Entry(self)
        self.entry_bloco = tk.Entry(self)
        self.entry_capacidade = tk.Entry(self)
        self.entry_estrutura = tk.Entry(self)

        self.botao_adicionar = tk.Button(self, text="Adicionar Sala", command=self.adicionar_sala)
        self.botao_exibir = tk.Button(self, text="Exibir Salas", command=exibir_salas)

        self.label_numero.grid(row=0, column=0)
        self.label_bloco.grid(row=1, column=0)
        self.label_capacidade.grid(row=2, column=0)
        self.label_estrutura.grid(row=3, column=0)

        self.entry_numero.grid(row=0, column=1)
        self.entry_bloco.grid(row=1, column=1)
        self.entry_capacidade.grid(row=2, column=1)
        self.entry_estrutura.grid(row=3, column=1)

        self.botao_adicionar.grid(row=4, column=0, columnspan=2, pady=10)
        self.botao_exibir.grid(row=5, column=0, columnspan=2)

    def adicionar_sala(self):
        numero_sala = int(self.entry_numero.get())
        bloco = self.entry_bloco.get()
        capacidade = int(self.entry_capacidade.get())
        estrutura = self.entry_estrutura.get()

        adicionar_sala(numero_sala, bloco, capacidade, estrutura)

# Lista objetos Sala
salas = []

# instância da interface
interface = Interface()
interface.mainloop()

# conexão com o MySQL
conexao.close()
