"""
Aplicações Distribuídas - Projeto 3- kuko_server.py
Grupo: 14
Números de aluno: 56699 58618
"""

from flask import Flask, request, jsonify
from kuko_data import KukoDB
import ssl


app = Flask(__name__)
kuko_db = KukoDB("kuko.db")



@app.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    question = data.get('question')
    answers = data.get('answers')
    k = data.get('k')
    if question and answers and k:
        question_id = kuko_db.add_quest(question, answers, k)
        return jsonify({"id": question_id, "message": "Question added successfully"}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400

@app.route('/question/<int:id_question>', methods=['GET'])
def get_question(id_question):
    question_data = kuko_db.selecionar_QUESTION(id_question)
    if question_data:
        return jsonify({'question_data': question_data}), 200
    else:
        return jsonify({'message': 'Question not found'}), 404

@app.route('/qset', methods=['POST'])
def add_qset():
    data = request.get_json()
    quest_ids = data.get('question_ids')
    if quest_ids:
        qset_id = kuko_db.inserir_QSET(quest_ids)
        return jsonify({"id": qset_id, "message": "QSet added successfully"}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400

@app.route('/qset/<int:id_qset>', methods=['GET'])
def get_qset(id_qset):
    qset_data = kuko_db.selecionar_QSET(id_qset)
    if qset_data:
        return jsonify({'qset_data': qset_data}), 200
    else:
        return jsonify({'message': 'QSet not found'}), 404

@app.route('/quiz', methods=['POST'])
def add_quiz():
    data = request.get_json()
    quest_set_id = data.get('quest_set_id')
    quiz_data = {
        "question_set": data.get('question_set'),
        "state": data.get('state'),
        "timestamp_p": data.get('timestamp_p'),
        "timestamp_e": data.get('timestamp_e'),
        "question_i": data.get('question_i'),
        "participants": data.get('participants')
    }
    if quest_set_id and quiz_data:
        quiz_id = kuko_db.inserir_Quiz(quest_set_id, quiz_data)
        return jsonify({"id": quiz_id, "message": "Quiz added successfully"}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400

@app.route('/quiz/<int:id_quiz>', methods=['GET'])
def get_quiz(id_quiz):
    quiz_data = kuko_db.selecionar_Quiz(id_quiz)
    if quiz_data:
        return jsonify({'quiz_data': quiz_data}), 200
    else:
        return jsonify({'message': 'Quiz not found'}), 404

@app.route('/launch/<int:id_quiz>', methods=['POST'])
def launch_quiz(id_quiz):
    # Lógica para lançar o quiz
    next.set(f"/quiz/{id_quiz}", b"next")
    return jsonify({'message': f'Quiz {id_quiz} launched successfully'}), 200

@app.route('/next/<int:id_quiz>', methods=['POST'])
def next_question(id_quiz):
    # Lógica para avançar para a próxima pergunta do quiz
    next.set(f"/quiz/{id_quiz}", b"next")
    return jsonify({'message': f'Next question for quiz {id_quiz}'}), 200

@app.route('/reg/<int:id_quiz>', methods=['POST'])
def register_participant(id_quiz):
    data = request.get_json()
    participant = data.get('participant')
    if kuko_db.register_participant(id_quiz, participant):
        return jsonify({'message': f'Participant {participant} registered for quiz {id_quiz}'}), 200
    else:
        return jsonify({'message': 'Error registering participant'}), 400

@app.route('/get/<int:id_quiz>', methods=['GET'])
def get_current_question(id_quiz):
    current_question = kuko_db.get_current_question(id_quiz)
    if current_question:
        return jsonify({'current_question': current_question}), 200
    else:
        return jsonify({'message': 'Current question not found'}), 404

@app.route('/ans/<int:id_quiz>', methods=['POST'])
def answer_question(id_quiz):
    data = request.get_json()
    answer = data.get('answer')
    participant = data.get('participant')
    if kuko_db.answer_question(id_quiz, participant, answer):
        return jsonify({'message': f'Answer {answer} registered for quiz {id_quiz}'}), 200
    else:
        return jsonify({'message': 'Error registering answer'}), 400

@app.route('/rel/<int:id_quiz>', methods=['GET'])
def get_report(id_quiz):
    next.set(f"/quiz/{id_quiz}", b"rel")
    report = kuko_db.get_report(id_quiz)
    if report:
        return jsonify({'report': report}), 200
    else:
        return jsonify({'message': 'Report not found'}), 404
    


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


