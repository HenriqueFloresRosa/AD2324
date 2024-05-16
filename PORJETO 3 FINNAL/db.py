import sqlite3
from os.path import isfile

def connect_db(dbname):
    # Verifica se o banco de dados já existe
    db_is_created = isfile(dbname)
    # Conecta ao banco de dados
    connection_db = sqlite3.connect(dbname)
    cursor = connection_db.cursor()

    # Cria as tabelas caso o banco de dados não exista
    if not db_is_created:
        cursor.execute('PRAGMA foreign_keys = ON;')

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS QUESTIONS (
                id_question INTEGER PRIMARY KEY AUTOINCREMENT,  
                question TEXT, 
                answers TEXT, 
                k INT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS QSET (
                id_set INTEGER PRIMARY KEY AUTOINCREMENT,   
                question TEXT NOT NULL, 
                FOREIGN KEY (question) REFERENCES QUESTIONS(id_question) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS QUIZ (
                id_quiz INTEGER PRIMARY KEY AUTOINCREMENT,  
                id_set INTEGER,     
                question_set VARCHAR, 
                state VARCHAR, 
                timestamp_p VARCHAR, 
                timestamp_e VARCHAR, 
                question_i VARCHAR, 
                participants INTEGER,
                FOREIGN KEY (id_set) REFERENCES QSET(id_set) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS RESULTS (
                id_results INTEGER PRIMARY KEY, 
                id_quiz INTEGER, 
                id_question INTEGER, 
                participant VARCHAR, 
                answer VARCHAR, 
                FOREIGN KEY (id_quiz) REFERENCES QUIZ(id_quiz) ON DELETE CASCADE, 
                FOREIGN KEY (id_question) REFERENCES QUESTIONS(id_question) ON DELETE CASCADE
            );
        """)

        connection_db.commit()
        print("Banco de dados criado com sucesso!")
    else:
        print("O banco de dados já existe.")

    return connection_db, cursor

def inserir_QUESTION(conn, cursor, question, answers, k):
    # Converte a lista de respostas em uma string separada por ponto e vírgula
    answers_str = ';'.join(answers)
    # Insere os dados na tabela QUESTIONS
    cursor.execute("INSERT INTO QUESTIONS (question, answers, k) VALUES (?, ?, ?)", (question, answers_str, k))
    conn.commit()

# Conecta ao banco de dados
conn, cursor = connect_db("kuko_data.db")


# Fechando a conexão com o banco de dados
conn.close()

def inserir_QSET(conn, cursor, quest_ids):
    # Inserir dados na tabela QSET
    cursor.execute("INSERT INTO QSET (questions) VALUES (?)", (quest_ids,))
    conn.commit()

def inserir_Quiz(conn, cursor, quest_set_id, quiz_data):
    # Inserir dados na tabela QUIZ
    cursor.execute("INSERT INTO QUIZ (id_set, question_set, state, timestamp_p, timestamp_e, question_i, participants) VALUES (?,?,?,?,?,?,?)", (quest_set_id, quiz_data[0], quiz_data[1], quiz_data[2], quiz_data[3], quiz_data[4], quiz_data[5]))
    conn.commit()

def inserir_RESULT(conn, cursor, quiz_id, quest_id, participant, answer):
    # Inserir dados na tabela RESULTS
    cursor.execute("INSERT INTO RESULTS (id_quiz, id_question, participant, answer) VALUES (?,?,?,?)", (quiz_id, quest_id, participant, answer))
    conn.commit()

def selecionar_QUESTION(conn, cursor, id_question):
    # Selecionar dados da tabela QUESTIONS
    cursor.execute("SELECT * FROM QUESTIONS WHERE id_question =?", (id_question,))
    conn.commit()
    return cursor.fetchone()

def selecionar_QSET(conn, cursor, id_set):
    # Selecionar dados da tabela QSET
    cursor.execute("SELECT * FROM QSET WHERE id_set =?", (id_set,))
    conn.commit()
    return cursor.fetchone()

def selecionar_Quiz(conn, cursor, id_quiz):
    # Selecionar dados da tabela QUIZ
    cursor.execute("SELECT * FROM QUIZ WHERE id_quiz =?", (id_quiz,))
    conn.commit()
    return cursor.fetchone()
