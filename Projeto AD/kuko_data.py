"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 XXXXX
"""
import time
import copy
from typing import Dict, List, Tuple

import time
from typing import List, Dict

class Question:
    def __init__(self, id_question: int, question_text: str, answers: List[str], correct_answer_index: int):
        self.id_question = id_question
        self.question_text = question_text
        self.answers = answers
        self.correct_answer_index = correct_answer_index

    def __str__(self):
        return f"Pergunta {self.id_question}: {self.question_text}"

class QSet:
    def __init__(self, id_set: int, question_ids: List[int]):
        self.id_set = id_set
        self.question_ids = question_ids

    def __str__(self):
        return f"QSet {self.id_set}: {self.question_ids}"

class Quiz:
    def __init__(self, id_quiz: int, id_set: int, question_set: List[Question], state: str = "PREPARED"):
        self.id_quiz = id_quiz
        self.id_set = id_set
        self.question_set = question_set
        self.state = state
        self.timestamp_P = 0  
        self.timestamp_E = 0 
        self.question_i = 0  
        self.participants = []
        self.replies = {}

    def __str__(self):
        return f"Quiz {self.id_quiz}: State - {self.state}, Questions - {self.question_set}"

class Kuko:
    def __init__(self):
        self.questions = {}
        self.qsets = {}
        self.quizzes = {}

    def create_question(self, id_question: int, question_text: str, answers: List[str], correct_answer_index: int):
        question = Question(id_question, question_text, answers, correct_answer_index)
        self.questions[id_question] = question
        return id_question

    def create_qset(self, id_set: int, question_ids: List[int]):
        qset = QSet(id_set, question_ids)
        self.qsets[id_set] = qset
        return id_set

    def create_quiz(self, id_quiz: int, id_set: int):
        if id_set not in self.qsets:
            return None
        question_set = [self.questions[question_id] for question_id in self.qsets[id_set].question_ids]
        quiz = Quiz(id_quiz, id_set, question_set)
        self.quizzes[id_quiz] = quiz
        return id_quiz

    def launch_quiz(self, id_quiz: int):
        if id_quiz not in self.quizzes:
            return False
        quiz = self.quizzes[id_quiz]
        if quiz.state != "PREPARED":
            return False
        quiz.state = "ONGOING"
        quiz.timestamp_P = int(time.time())
        return True

# Example usage:
# kuko = Kuko()
# q1 = kuko.create_question(1, "What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2)
# q2 = kuko.create_question(2, "Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 1)
# qset = kuko.create_qset(1, [1, 2])
# quiz = kuko.create_quiz(1, 1)
# kuko.launch_quiz(1)



     
        


    

