"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import copy
import sqlite3
from db import *

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
class KUKO:
    
    
    def __init__(self, db_file):
        self.connection_db = sqlite3.connect(db_file)
        self.cursor = self.connection_db.cursor()
        self.question_id_counter = 0  # Inicializa o contador de ID de perguntas

    def add_quest(self, question_text, options, correct_option_index):
        # Incrementa o contador de ID de perguntas
        self.question_id_counter += 1
        id_quest = self.question_id_counter
        
        quest = Question(id_quest, question_text, options, correct_option_index)

        # Insere dados na tabela "question"
        self.cursor.execute("INSERT INTO question (id_question, question, answer, k) VALUES (?, ?, ?, ?)",
                            (quest.id_question, quest.question, quest.answers[correct_option_index], quest.k))

        self.connection_db.commit()
        return "Nova pergunta: " + str(id_quest)


    def add_quest_set(self, quest_ids):
        id_set = int(time.time() * 1000)

        # Inserir dados na tabela q_set
        self.cursor.execute("INSERT INTO q_set (id_set, question) VALUES (?, ?)",
                            (id_set, ','.join(map(str, quest_ids))))

        self.connection_db.commit()
        return "OK;" + str(id_set)

    def add_quiz(self, quiz_data):
        quest_set_id = int(quiz_data[0])
        if quest_set_id not in list(self._quest_sets.keys()):
            return "NOK"
        elif self._quest_sets.get(quest_set_id).num_quest() != len(quiz_data[1:]):
            return "NOK"
        else:
            quiz_id = int(time.time() * 1000)

            quest_points = {}
            for i in range(self._quest_sets.get(quest_set_id).num_quest()):
                quest_points[int(self._quest_sets.get(quest_set_id).quest_ids[i])] = int(quiz_data[i + 1])

            quiz = Quiz(quest_set_id, quest_points)

            # Inserir dados na tabela quiz
            self.cursor.execute("INSERT INTO quiz (id_quiz, id_set, question_set) VALUES (?, ?, ?)",
                                (quiz_id, quiz.id_set, ','.join(map(str, quiz.quest_set))))

            self.connection_db.commit()
            return "OK;" + str(quiz_id)


    def start_quiz(self, quiz_id):
        if quiz_id not in list(self._quizzes.keys()):
            return "NOK"
        else:
            self._quizzes[quiz_id].state = "ONGOING"
            self._quizzes[quiz_id].timestamp_start = int(time.time())
            return "OK"
        self.cursor.execute
