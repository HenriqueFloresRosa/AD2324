"""
Aplicações Distribuídas - Projeto 1 - kuko_data.py
Grupo: 14
Números de aluno: 56699 58618
"""

import time
import copy
import sqlite3

class Question:
    id_counter = 0

    def __init__(self, question_text, options, correct_option_index):
        Question.id_counter += 1
        self.id_quest = Question.id_counter
        self.question_text = question_text
        self.options = copy.deepcopy(options)
        self.correct_option = correct_option_index

    def __str__(self):
        return f"{self.id_quest};{self.question_text};{';'.join(self.options)};{self.correct_option}"

class QuestSet:
    id_counter = 0

    def __init__(self, quest_ids):
        QuestSet.id_counter += 1
        self.id_set = QuestSet.id_counter
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
        quest_set = QuestSet(quest_ids)
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
    def __init__(self):
        self._quests = {}
        self._quest_sets = {}
        self._quizzes = {}

    def add_quest(self, question_text, options, correct_option_index):
        id_quest = int(time.time() * 1000)  
        quest = Question(question_text, options, correct_option_index)
        self._quests[id_quest] = quest
        return "OK;" + str(id_quest)
        
    def add_quest_set(self, quest_ids):
        id_set = int(time.time() * 1000)  
        quest_set = QuestSet(quest_ids)
        self._quest_sets[id_set] = quest_set
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
                quest_points[int(self._quest_sets.get(quest_set_id).quest_ids[i])] = int(quiz_data[i+1])
            
            quiz = Quiz(quest_set_id, quest_points)
            self._quizzes[quiz_id] = quiz
            return "OK;" + str(quiz_id)
    
    def launch_quiz(self, quiz_id):
        quiz_id = int(quiz_id)
        if quiz_id not in list(self._quizzes.keys()):
            return "NOK"
        elif self._quizzes[quiz_id].state == "PREPARED":
            self._quizzes[quiz_id].state = "ONGOING"
            return "OK"
        else:
            return "NOK"
    
    def register_participant(self, registration_data):
        quiz_id = int(registration_data[0])
        user_id = int(registration_data[1])
        
        if quiz_id not in list(self._quizzes.keys()):
            return "NOK"
        elif self._quizzes[quiz_id].state == "PREPARED":
            self._quizzes[quiz_id].participants.append(user_id)
            self._quizzes[quiz_id].responses[user_id] = []
            return "OK"
        else:
            return "NOK"

    def get_current_question(self, quiz_data):
        quiz_id = int(quiz_data[0])
        user_id = int(quiz_data[1])

        if quiz_id not in list(self._quizzes.keys()):
            return "NOK"
        elif self._quizzes[quiz_id].state != "ONGOING":
            return "NOK"
        elif user_id in self._quizzes[quiz_id].participants:
            current_question_id = self._quizzes[quiz_id].current_quest_index
            question = self._quests.get(current_question_id)
            return "OK;" + str(question)
        else:
            return "NOK"
    
    def get_question_set_answers(self, quiz_id):
        answers = []
        quest_set_id = self._quizzes[quiz_id].id_set
        
        for question_id in self._quest_sets.get(quest_set_id).quest_ids:
            answers.append(self._quests[int(question_id)].correct_option)
        return answers

