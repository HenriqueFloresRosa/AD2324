from flask import Flask, request, jsonify
from kuko_data import KukoDB

app = Flask(__name__)
kuko_db = KukoDB("kuko_data.db")

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
    quest_ids = data.get('quest_ids')
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
    quiz_data = data.get('quiz_data')
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



@app.route('/launch', methods=['POST'])
def Quiz_game(ola):
    return ola

@app.route('/next', methods =['POST'])
def next_question(next):
    return next
@app.route('/reg', methods =['POST'])
def registrar_participant(id_participant):
    return id_participant

@app.route('/get', methods=['POST'])
def obter_pergunta(id_question):
    return id_question
@app.route('/ans', methods =['POST'])
def registrar_reposta(id_participant,id_question,k):
    return (id_participant,id_question,k)
@app.route('/rel ', methods =['GET'])
def dnsaknjnsf():
    return 

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


