"""
Aplicações Distribuídas - Projeto 3- kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import copy
from typing import Dict, List
from db import connect_bd

class Question:
    id_counter = 0

    def __init__(self, id_question, question, answers, k):
        self.id_question = id_question
        self.question = question
        self.answers = copy.deepcopy(answers)
        self.k = k

    def __str__(self):
        return f"{self.id_question};{self.question};{';'.join(self.answers)};{self.k}"

class QSet:
    id_counter = 0

    def __init__(self, quest_ids):
        self.id_set = QSet.id_counter
        self.quest_ids = copy.deepcopy(quest_ids)

    def num_quest(self):
        return len(self.quest_ids)

    def __str__(self):
        return f"QuestSet {self.id_set}: {self.quest_ids}"

class QuizGame:
    def __init__(self):
        self.quests = {}
        self.quest_sets = {}
        self.quizzes = {}

    def create_quest(self, question_text, options, correct_option_index):
        quest = Question(question_text, options, correct_option_index)
        self.quests[quest.id_quest] = quest
        return quest.id_quest

    def create_quest_set(self, quest_ids):
        quest_set = QSet(quest_ids)
        self.quest_sets[quest_set.id_set] = quest_set
        return quest_set.id_set

    def create_quiz(self, id_set, *points):
        if id_set not in self.quest_sets:
            return None
        
        quest_set = [self.quests[quest_id] for quest_id in self.quest_sets[id_set].quest_ids]
        quiz_id = int(time.time() * 1000)  
        quiz = Quiz(id_set, quest_set)
        self.quizzes[quiz_id] = quiz
        return quiz_id

    def start_quiz(self, id_quiz):
        if id_quiz not in self.quizzes:
            return "NOK"
        
        quiz = self.quizzes[id_quiz]
        if quiz.state != "PREPARED":
            return "NOK"
        
        quiz.state = "ONGOING"
        quiz.timestamp_start = int(time.time())
        return "OK"

    def get_result(self, quiz_id):
        quiz_id = int(quiz_id)

        if quiz_id not in self.quizzes:
            return "NOK"
        else:
            quiz = self.quizzes[quiz_id]
            total_questions = len(quiz.quest_set)
            results = []
            
            for participant, responses in quiz.responses.items():
                correct_answers = sum(responses)
                score = correct_answers * 20
                results.append(f"{quiz_id};acertou {correct_answers} em {total_questions}, com pontuação {score}")

            return results

class Quiz:
    def __init__(self, id_set, quest_set, state="PREPARED"):
        self.id_quiz = int(time.time() * 1000)  
        self.id_set = id_set
        self.quest_set = quest_set
        self.state = state
        self.timestamp_start = 0  
        self.current_quest_index = 0  
        self.participants = []
        self.responses = {}

    def __str__(self):
        return f"Quiz {self.id_quiz}: State - {self.state}, Questions - {self.quest_set}"


class KukoDB:
    def __init__(self, dbname):
        self.conn, self.cursor = connect_bd(dbname)

    def add_quest(self, question, answers, k):
        answers_str = ';'.join(answers)
        self.cursor.execute("INSERT INTO question (question, answer, k) VALUES (?, ?, ?)", (question, answers_str, k))
        self.conn.commit()
        return self.cursor.lastrowid

    def selecionar_QUESTION(self, id_question):
        self.cursor.execute("SELECT * FROM question WHERE id_question = ?", (id_question,))
        return self.cursor.fetchone()

    def inserir_QSET(self, quest_ids):
        self.cursor.execute("INSERT INTO q_set (question) VALUES (?)", (','.join(map(str, quest_ids)),))
        self.conn.commit()
        return self.cursor.lastrowid

    def selecionar_QSET(self, id_set):
        self.cursor.execute("SELECT * FROM q_set WHERE id_set = ?", (id_set,))
        return self.cursor.fetchone()

    def inserir_Quiz(self, quest_set_id, quiz_data):
        self.cursor.execute("INSERT INTO quiz (id_set, question_set, state, timestamp_p, timestamp_e, question_i, participants) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (quest_set_id, quiz_data['question_set'], quiz_data['state'], quiz_data['timestamp_p'], quiz_data['timestamp_e'], quiz_data['question_i'], quiz_data['participants']))
        self.conn.commit()
        return self.cursor.lastrowid

    def selecionar_Quiz(self, id_quiz):
        self.cursor.execute("SELECT * FROM quiz WHERE id_quiz = ?", (id_quiz,))
        return self.cursor.fetchone()
