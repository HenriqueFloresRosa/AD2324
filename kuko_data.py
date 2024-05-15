"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import sqlite3
from typing import List, Dict

class KUKO:
    def __init__(self,db:str):
        self.db = db

    def envia_Question( self, questions: str, answers: str, k: int): # POST SUPER IMPORTANTE VAI SER IGUAL NOS OUTROS
        connection_db = sqlite3.connect(self.db)
        cursor = connection_db.cursor()
     
        # Inserir dados na tabela "QUESTION"
        cursor.execute("INSERT INTO question (questions, answers, k) VALUES (?, ?, ?, ?)",
                            (questions, answers,k))
        connection_db.commit()
        c = cursor.lastrowid
        connection_db.close()
        return f"Nova pergunta: {c}"
    
 

    def envia_Qset(self, quest_ids: List[int]):
        id_set = int(time.time() * 1000)
        # Inserir dados na tabela QSET
        self.cursor.execute("INSERT INTO qset (id, questions) VALUES (?, ?)",
                            (id_set, ','.join(map(str, quest_ids))))
        self.connection_db.commit()
        return f"OK; {id_set}"

    def envia_Quiz(self, quiz_data: List[int]):
        quest_set_id = int(quiz_data[0])
        # Verificar se o conjunto de perguntas existe e se o número de perguntas corresponde
        if quest_set_id not in self._quest_sets:
            return "NOK"
        elif len(self._quest_sets[quest_set_id].quest_ids) != len(quiz_data[1:]):
            return "NOK"
        else:
            quiz_id = int(time.time() * 1000)
            quest_points = {int(self._quest_sets[quest_set_id].quest_ids[i]): int(quiz_data[i + 1]) for i in range(len(quiz_data[1:]))}
            quiz = (quest_set_id, quest_points, self)

            # Inserir dados na tabela quiz
            self.cursor.execute("INSERT INTO quiz (id, status, timestamp_p, current_question, participants) VALUES (?, ?, ?, ?, ?)",
                                (quiz_id, quiz.state, quiz.timestamp_P, quiz.questions_i, ','.join(map(str, quiz.participants))))
            self.connection_db.commit()
            return f"OK; {quiz_id}"

    def getQuestions(self):
        self.cursor.execute("SELECT * FROM question")
        questions = self.cursor.fetchall()
        return questions

    def getQuestSets(self):
        self.cursor.execute("SELECT * FROM qset")
        quest_sets = self.cursor.fetchall()
        return quest_sets

    def getQuizzes(self):
        self.cursor.execute("SELECT * FROM quiz")
        quizzes = self.cursor.fetchall()
        return quizzes


    def getQuizzes(self):
        self.cursor.execute("SELECT * FROM quiz")
        quizzes = self.cursor.fetchall()
        return quizzes
