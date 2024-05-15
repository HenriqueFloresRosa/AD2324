"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import copy
"import sqlite3
"from db import *
from typing import Dict, List, Tuple


class Question:
    

    def __init__(self, answers: List[str], k: int, question=str, Kukodata):
        self.id_question = len(Kukodata.getQuestions()) + 1
        self.question = question  # pergunta
        self.answers = answers  # respostas admitidas
        self.k = k  # resposta correta

    def ID(self):
        return self.id_question

    def __str__(self):
        return f"{self.id_question};{';'.join(self.answers)}"

class QuestionSet:

    def __init__(self, questions, Kukodata):
        self.id_set = len(Kukodata.getQuestSets()) + 1
        self.quest_ids = questions

    def ID (self):
        return self.id_set



class Quiz:
    def __init__(self, id_set, score_set, Kukodata):
        self.id_quiz = len(Kukodata.getQuizzes()) + 1
        self.id_set = id_set

        questions = []
        i = 0
        for question in Kukodata.getQuestions()[id_set ].questions:
            questionCopy = copy.deepcopy(Kukodata.getQuestions().questions[question])
            questions.append(questionCopy,score_set[i])
            i += 1

            self.questions_set = questions

            self.state = "PREPARED"
            self.timestamp_P = time.time()
            self.timestamp_E = None
            self.timestamp_i = 0
            self.questions_i = 0
            self.participants = []
            self.replies = {}

    def regsitar_participantes(self, participant_id):
        self.participants.append(participant_id)
        self.replies[participant_id] = []
        for question in self.questions_set:
            self.replies[participant_id].append(0)

    def começar_quiz(self):
        self.state = "ONGOING"

    def getIDquiz(self):
        return self.id_quiz
    
    def buscar_Participante(self):
        return self.participants
    
    def buscar_correnteQuestion(self):
        return self.questions_set[self.questions_i][0]
    
    def ProximaQuestion(self):
        self.questions_i += 1
        
        if self.questions_i >= len(self.questions_set):
            self.questions_i = 0
            self.state = "ENDED"
            self.timestamp_E = time.time()
        
        return self.questions_set[self.questions_i][0]
    
    def responderQuiz(self, id_answer, id_participant):
        return self.replies[id_participant][self.question_i] = id_answer


    def getRelatorio(self, id_pariticipante):
        participanteAnswers = self.relpies[id_participant}
        corretoN = 0
        pontua = 0
        i = 0
        for question in self.question_set:
            scores.append(i[1])

            respostas += str(i[1])+" points ## id "+str(id[0].getId())+" ## "+str(id[0])+" ("+str(id[0].k)+")\n"

        participantes = ""

        for i in self.getParticipants().items():
            participantes += "Participante: "+str(i[0])+", Respostas: "+str(i[1])+"\n"

        return f"ID do Quiz: 1\n \
                Estado: {self.state}\n \
                Pontos p/pergunta: {scores} \n \
                Pergunta atual: {self.question_i} \n \
                Número de participantes: {len(self.participants)} \n \
                Iniciado a: {self.timestamp_P} \n \
                Terminado a: {self.timestamp_E} \n \
                Perguntas e R: \n \
                {respostas} \
                {participantes}"
        
        
        

#########################################################################################################

class KUKO:
    
    
    def __init__(self, db_file):
        self.connection_db = sqlite3.connect(db_file)
        self.cursor = self.connection_db.cursor()
        self.question_id_counter = 0

    def addquestion(self,id_question, questions, answers, k):
        #
        id_question = self.question_id_counter
        
        quest = Question(id_question, questions, answers, k)

        # Insere dados na tabela "question"
        self.cursor.execute("INSERT INTO question (id_question, questions, answers, k) VALUES (?, ?, ?, ?)",
                            (quest.id_question, quest.question, quest.answers[k], quest.k))

        self.connection_db.commit()
        return "Nova pergunta: " + str(id_question)


    def addqset(self, quest_ids):
        id_set = int(time.time() * 1000)

        # Inserir dados na tabela q_set
        self.cursor.execute("INSERT INTO q_set (id_set, question) VALUES (?, ?)",
                            (id_set, ','.join(map(str, quest_ids))))

        self.connection_db.commit()
        return "OK;" + str(id_set)

    def addquiz(self, quiz_data):
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


    #def start_quiz(self, quiz_id):
        if quiz_id not in list(self._quizzes.keys()):
            return "NOK"
        else:
            self._quizzes[quiz_id].state = "ONGOING"
            self._quizzes[quiz_id].timestamp_start = int(time.time())
            return "OK"
        self.cursor.execute
