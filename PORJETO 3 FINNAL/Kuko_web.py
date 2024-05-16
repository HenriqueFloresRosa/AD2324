from flask import Flask, request, jsonify
import kuko_data

app = Flask(__name__)

@app.route('/question', methods=['POST'])
def question():
    data = request.get_json()
    if data["question"] and data["answers"] and data["k"]:
        devolve = kuko_data.inserir_QUESTION(data["question"], data["answers"], data["k"])
        return jsonify(devolve), 200
    else:
        return jsonify({"message": "Missing data"}), 400

@app.route('/question/<int:quetion_id>', methods=['GET'])
def questionget(question_id = None):
    devolve = kuko_data.selecionar_QUESTION(question_id)
    return jsonify(devolve), 200

@app.route('/qset', methods=['POST'])
def Qset(id_set, id_question):
    
    if id_set and id_question:
        devolve = kuko_data.inserir_QSET(id_set, id_question)
        return jsonify(devolve), 200
    else:
        return jsonify({"message": "Missing data"}), 400

@app.route('/qset/<int:qset_id>', methods=['GET'])
def Qsetget(qset_id = None):


























