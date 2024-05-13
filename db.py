import sqlite3
from os.path import isfile

def bd():
    db_criada = isfile('kuko.db')
    connection_db = sqlite3.connect('kuko.db')
    cursor = connection_db.cursor()

    if not db_criada:
        cursor.execute('PRAGMA foreign_keys = ON;')

        cursor.execute("""
            CREATE TABLE question (
                id_question INTEGER PRIMARY KEY AUTOINCREMENT,  
                question TEXT NO NULL VARCHAR, 
                answer TEXT NO NULL VARCHAR, 
                k INT NOT NULL
            );
        """)
        
        cursor.execute("""
            CREATE TABLE q_set (
                id_set INTEGER PRIMARY KEY AUTOINCREMENT,   
                question TEXT NOT NULL, 
                FOREIGN KEY (question) REFERENCES question(id_question) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE quiz (
                id_quiz INTEGER PRIMARY KEY, 
                id_set VARCHAR, 
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
            CREATE TABLE results (
                id_results INTEGER PRIMARY KEY, 
                id_quiz VARCHAR, 
                id_question VARCHAR, 
                participant VARCHAR, 
                answer VARCHAR, 
                FOREIGN KEY (id_quiz) REFERENCES quiz(id_quiz) ON DELETE CASCADE, 
                FOREIGN KEY (id_question) REFERENCES question(id_question) ON DELETE CASCADE
            );
        """)
        
        connection_db.commit()

    else:
        return "Base de Dados já existe/foi criada"
    
    connection_db.close()

    