"""
Aplicações Distribuídas - Projeto 3- populate_db.py
Grupo: 14
Números de aluno: 56699 58618
"""
import sqlite3

def populate_db(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()

    # Inserir dados iniciais na tabela 'question'
    cursor.execute("""
        INSERT INTO question (question, answer, k) 
        VALUES 
        ('Qual foi o campeão da Liga Portuguesa na temporada 23/24?', 'A. Porto;B. Benfica;C. Sporting;D. Braga', 3),
        ('Quem foi o artilheiro da Liga Portuguesa na temporada 23/24?', 'A. Di Maria;B. Gyokeres;C. Banza;D. Paulinho', 2),
        ('Qual foi o clube que ficou em último lugar na Liga Portuguesa na temporada 23/24?', 'A. Portimense;B. Boavista;C. Estrela;D. Farense', 1),
        ('Quantos clubes participaram na Liga Portuguesa na temporada 23/24?', 'A. 16;B. 18;C. 20;D. 22', 2),
        ('Qual foi o resultado do clássico entre Porto e Benfica na temporada 23/24?', 'A. 0-0;B. 1-1;C. 2-2;D. 5-0', 4)
    """)

    # Inserir dados iniciais na tabela 'q_set'
    cursor.execute("""
        INSERT INTO q_set (question) 
        VALUES 
        ('2,3,4,5'),
        ('3,1,2,4'),
        ('1,2,3,4,5')
    """)

    # Inserir dados iniciais na tabela 'quiz'
    cursor.execute("""
        INSERT INTO quiz (id_set, question_set, state, timestamp_p, timestamp_e, question_i, participants) 
        VALUES 
        (1, '1,2,3,4,5', 'active', '2024-05-01T10:00:00Z', '2024-05-01T11:00:00Z', '1', 5)
    """)

    # Inserir dados iniciais na tabela 'results'
    cursor.execute("""
        INSERT INTO results (id_quiz, id_question, participant, answer) 
        VALUES 
        (1, 1, 'John Doe', 'A'),
        (1, 2, 'Jane Smith', 'B'),
        (1, 3, 'Alice Johnson', 'C'),
        (1, 4, 'Bob Brown', 'D'),
        (1, 5, 'Charlie Davis', 'A')
    """)

    connection.commit()
    connection.close()
    print(f"Database '{dbname}' populated successfully.")

if __name__ == "__main__":
    populate_db('kuko.db')

