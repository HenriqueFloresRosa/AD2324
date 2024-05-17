import requests
import json

class QuizClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_request(self, endpoint, method="GET", data=None):
        url = f"{self.server_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": response.text}
        except Exception as e:
            return {"error": str(e)}

    def question(self, question, answers, k):
        data = {
            "question": question,
            "answers": answers,
            "k": k
        }
        return self.send_request("question", "POST", data)

    def question_get(self, id_question):
        return self.send_request(f"question/{id_question}")

    def qset(self, question_ids):
        data = {
            "question_ids": question_ids
        }
        return self.send_request("qset", "POST", data)

    def quiz(self, quest_set_id, state, timestamp_p, timestamp_e, question_i, participants):
        data = {
            "quest_set_id": quest_set_id,
            "state": state,
            "timestamp_p": timestamp_p,
            "timestamp_e": timestamp_e,
            "question_i": question_i,
            "participants": participants
        }
        return self.send_request("quiz", "POST", data)

    def quiz_get(self, id_quiz):
        return self.send_request(f"quiz/{id_quiz}")

    def launch(self, id_quiz):
        return self.send_request(f"launch/{id_quiz}", "POST")

    def next_question(self, id_quiz):
        return self.send_request(f"next/{id_quiz}", "POST")

    def register_participant(self, id_quiz, participant):
        data = {
            "participant": participant
        }
        return self.send_request(f"reg/{id_quiz}", "POST", data)

    def get_current_question(self, id_quiz):
        return self.send_request(f"get/{id_quiz}")

    def answer_question(self, id_quiz, answer):
        data = {
            "answer": answer
        }
        return self.send_request(f"ans/{id_quiz}", "POST", data)

    def get_report(self, id_quiz):
        return self.send_request(f"rel/{id_quiz}")

def main():
    client = QuizClient("http://localhost:5000")
    
    while True:
        user_input = input('comando > ').strip()
        cmd = user_input.split(';')
        
        if cmd[0] == "QUESTION":
            question = cmd[1]
            answers = cmd[2:-1]
            k = int(cmd[-1])
            response = client.question(question, answers, k)
            print(response)
        elif cmd[0] == "QUESTIONGET":
            id_question = int(cmd[1])
            response = client.question_get(id_question)
            print(response)
        elif cmd[0] == "QSet":
            question_ids = [int(id) for id in cmd[1:]]
            response = client.qset(question_ids)
            print(response)
        elif cmd[0] == "QUIZ":
            quest_set_id = int(cmd[1])
            state = cmd[2]
            timestamp_p = cmd[3]
            timestamp_e = cmd[4]
            question_i = cmd[5]
            participants = int(cmd[6])
            response = client.quiz(quest_set_id, state, timestamp_p, timestamp_e, question_i, participants)
            print(response)
        elif cmd[0] == "QUIZGET":
            id_quiz = int(cmd[1])
            response = client.quiz_get(id_quiz)
            print(response)
        elif cmd[0] == "LAUNCH":
            id_quiz = int(cmd[1])
            response = client.launch(id_quiz)
            print(response)
        elif cmd[0] == "NEXT":
            id_quiz = int(cmd[1])
            response = client.next_question(id_quiz)
            print(response)
        elif cmd[0] == "REG":
            id_quiz = int(cmd[1])
            participant = cmd[2]
            response = client.register_participant(id_quiz, participant)
            print(response)
        elif cmd[0] == "GET":
            id_quiz = int(cmd[1])
            response = client.get_current_question(id_quiz)
            print(response)
        elif cmd[0] == "ANS":
            id_quiz = int(cmd[1])
            answer = cmd[2]
            response = client.answer_question(id_quiz, answer)
            print(response)
        elif cmd[0] == "REL":
            id_quiz = int(cmd[1])
            response = client.get_report(id_quiz)
            print(response)
        else:
            print("Comando desconhecido!")

if __name__ == "__main__":
    main()
