"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import copy
import sqlite3
from typing import List, Dict

class Question:
    def __init__(self, answers: List[str], k: int, question: str, Kukodata):
        self.id_question = len(Kukodata.getQuestions()) + 1
        self.question = question  # pergunta
        self.answers = answers  # respostas admitidas
        self.k = k  # resposta correta

    def IDQUESTION(self):
        return self.id_question

    def __str__(self):
        return f"{self.id_question};{self.question};{';'.join(self.answers)}"

class QuestionSet:
    def __init__(self, questions: List[int], Kukodata):
        self.id_set = len(Kukodata.getQuestSets()) + 1
        self.quest_ids = questions

    def IDQSET(self):
        return self.id_set

class QuizGame:
    def __init__(self, id_set: int, score_set: Dict[int, int], Kukodata):
        self.id_quiz = len(Kukodata.getQuizzes()) + 1
        self.id_set = id_set

        questions = []
        for question_id in Kukodata.getQuestions()[id_set].questions:
            question_copy = copy.deepcopy(Kukodata.getQuestions().questions[question_id])
            questions.append((question_copy, score_set[question_id]))

        self.questions_set = questions
        self.state = "PREPARED"
        self.timestamp_P = time.time()
        self.timestamp_E = None
        self.timestamp_i = 0
        self.questions_i = 0
        self.participants = []
        self.replies = {}

    def register_participant(self, participant_id: int):
        self.participants.append(participant_id)
        self.replies[participant_id] = [0] * len(self.questions_set)

    def start_quiz(self):
        self.state = "ONGOING"

    def getIDquiz(self):
        return self.id_quiz

    def getParticipants(self):
        return self.participants

    def getCurrentQuestion(self):
        return self.questions_set[self.questions_i][0]

    def nextQuestion(self):
        self.questions_i += 1
        if self.questions_i >= len(self.questions_set):
            self.questions_i = 0
            self.state = "ENDED"
            self.timestamp_E = time.time()
        return self.questions_set[self.questions_i][0]

    def answerQuestion(self, id_answer: int, id_participant: int):
        self.replies[id_participant][self.questions_i] = id_answer

    def getReport(self, id_participant: int):
        participant_answers = self.replies[id_participant]
        correct_count = 0
        score = 0
        scores = []
        respostas = ""
        for i, (question, points) in enumerate(self.questions_set):
            scores.append(points)
            respostas += f"{points} points ## id {question.ID()} ## {question} ({question.k})\n"

        participantes = ""
        for participant, answers in self.replies.items():
            participantes += f"Participante: {participant}, Respostas: {answers}\n"

        return (f"ID do Quiz: {self.id_quiz}\n"
                f"Estado: {self.state}\n"
                f"Pontos p/pergunta: {scores} \n"
                f"Pergunta atual: {self.questions_i} \n"
                f"Número de participantes: {len(self.participants)} \n"
                f"Iniciado a: {self.timestamp_P} \n"
                f"Terminado a: {self.timestamp_E} \n"
                f"Perguntas e R: \n{respostas}"
                f"{participantes}")

class KUKO:
    def __init__(self, db_file: str):
        self.connection_db = sqlite3.connect(db_file)
        self.cursor = self.connection_db.cursor()
        self.question_id_counter = 0

    def addQuestion(self, question_text: str, answers: List[str], k: int):
        self.question_id_counter += 1
        question = Question(answers, k, question_text, self)

        # Inserir dados na tabela "QUESTION"
        self.cursor.execute("INSERT INTO question (id, question_text, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (self.question_id_counter, question.question, question.answers[0], question.answers[1], question.answers[2], question.answers[3], question.k))
        self.connection_db.commit()
        return f"Nova pergunta: {self.question_id_counter}"

    def addQset(self, quest_ids: List[int]):
        id_set = int(time.time() * 1000)
        # Inserir dados na tabela QSET
        self.cursor.execute("INSERT INTO qset (id, questions) VALUES (?, ?)",
                            (id_set, ','.join(map(str, quest_ids))))
        self.connection_db.commit()
        return f"OK; {id_set}"

    def addQuiz(self, quiz_data: List[int]):
        quest_set_id = int(quiz_data[0])
        # Verificar se o conjunto de perguntas existe e se o número de perguntas corresponde
        if quest_set_id not in self._quest_sets:
            return "NOK"
        elif len(self._quest_sets[quest_set_id].quest_ids) != len(quiz_data[1:]):
            return "NOK"
        else:
            quiz_id = int(time.time() * 1000)
            quest_points = {int(self._quest_sets[quest_set_id].quest_ids[i]): int(quiz_data[i + 1]) for i in range(len(quiz_data[1:]))}
            quiz = Quiz(quest_set_id, quest_points, self)

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
