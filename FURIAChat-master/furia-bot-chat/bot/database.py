import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'quizzes.db')

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quiz (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                alternativa_a TEXT NOT NULL,
                alternativa_b TEXT NOT NULL,
                alternativa_c TEXT NOT NULL,
                correta TEXT NOT NULL
            )
        """)
        conn.commit()

criar_tabela()
print("Tabela 'quiz' criada com sucesso!")

def inserir_pergunta(pergunta, a, b, c, correta):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO quiz (pergunta, alternativa_a, alternativa_b, alternativa_c, correta) VALUES (?, ?, ?, ?, ?)",
            (pergunta, a, b, c, correta)
        )
        conn.commit()

def obter_pergunta_aleatoria():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM quiz ORDER BY RANDOM() LIMIT 1")
        return cursor.fetchone()
