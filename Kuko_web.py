import sys
from flask import Flask, request, jsonify
from kuko_data import KUKO

app = Flask(__name__)
kuko_data = KUKO()  # Instanciando a classe KukoData para lidar com as operações de banco de dados


@app.route('/question', methods=['POST', 'GET'])
def handle_question():
    if request.method == 'POST':
        # Implemente a lógica para adicionar uma nova pergunta
        question_info = request.json  # Aqui você pode acessar os dados JSON enviados pelo cliente
        question_id = kuko_data.add_question(question_info)
        if question_id:
            return jsonify({"status": "OK", "question_id": question_id}), 201
        else:
            return jsonify({"status": "NOK"}), 400
    elif request.method == 'GET':
        # Implemente a lógica para obter todas as perguntas cadastradas
        questions = kuko_data.get_all_questions()
        return jsonify(questions), 200


@app.route('/qset', methods=['POST', 'GET'])
def handle_qset():
    if request.method == 'POST':
        # Logica de POST
        qset_info = request.json  # Aqui você pode acessar os dados JSON enviados pelo cliente
        qset_id = kuko_data.add_question_set(qset_info)
        if qset_id:
            return jsonify({"status": "OK", "qset_id": qset_id}), 201
        else:
            return jsonify({"status": "NOK"}), 400
    elif request.method == 'GET':
        # Logica de GET
        qsets = kuko_data.get_all_question_sets()
        return jsonify(qsets), 200


@app.route('/quizgame', methods=['POST', 'GET'])
def handle_quizgame():
    if request.method == 'POST':
        # Logica de POST
        quiz_info = request.json  # Aqui você pode acessar os dados JSON enviados pelo cliente
        quiz_id = kuko_data.add_quiz(quiz_info)
        if quiz_id:
            return jsonify({"status": "OK", "quiz_id": quiz_id}), 201
        else:
            return jsonify({"status": "NOK"}), 400
        
    elif request.method == 'GET':
        # Logica de GET
        qsets = kuko_data.get_all_question_sets()
        return jsonify(qsets), 200


def main():
    if len(sys.argv) != 3:
        print("Usage: python kuko_server.py <host> <port>")
        return

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port)


if __name__ == "__main__":
    main()
