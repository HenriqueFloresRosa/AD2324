"""
Aplicações Distribuídas - Projeto 3- db.py
Grupo: 14
Números de aluno: 56699 58618
"""

import sqlite3
from os.path import isfile

def connect_bd(dbname):
    db_created = isfile(dbname)
    connection = sqlite3.connect(dbname)  
    cursor = connection.cursor()

    if not db_created:
        cursor.execute('PRAGMA foreign_keys = ON;')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS question (
                id_question INTEGER PRIMARY KEY AUTOINCREMENT,  
                question TEXT NOT NULL, 
                answer TEXT NOT NULL, 
                k INT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS q_set (
                id_set INTEGER PRIMARY KEY AUTOINCREMENT,   
                question TEXT NOT NULL, 
                FOREIGN KEY (question) REFERENCES question(id_question) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quiz (
                id_quiz INTEGER PRIMARY KEY AUTOINCREMENT,  
                id_set INTEGER,     
                question_set VARCHAR, 
                state VARCHAR, 
                timestamp_p VARCHAR, 
                timestamp_e VARCHAR, 
                question_i VARCHAR, 
                participants INTEGER,
                FOREIGN KEY (id_set) REFERENCES q_set(id_set) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id_results INTEGER PRIMARY KEY, 
                id_quiz INTEGER, 
                id_question INTEGER, 
                participant VARCHAR, 
                answer VARCHAR, 
                FOREIGN KEY (id_quiz) REFERENCES quiz(id_quiz) ON DELETE CASCADE, 
                FOREIGN KEY (id_question) REFERENCES question(id_question) ON DELETE CASCADE
            );
        """)

        connection.commit()
        print("Banco de dados criado com sucesso!")
    else:
        print("Base de Dados já existe/foi criada")
    
    return connection, cursor

# Testar a criação da base de dados
if __name__ == "__main__":
    connect_bd("kuko.db")

