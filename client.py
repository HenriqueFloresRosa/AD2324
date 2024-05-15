from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db_file = ''

def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    question_text = data['question_text']
    option1 = data['option1']
    option2 = data['option2']
    option3 = data['option3']
    option4 = data['option4']
    correct_option = data['correct_option']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO question (question_text, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)",
        (question_text, option1, option2, option3, option4, correct_option)
    )
    conn.commit()
    question_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": question_id, "message": "Question added successfully"}), 201

@app.route('/question', methods=['GET'])
def get_question():
    question_id = request.args.get('id')
    conn = get_db_connection()
    question = conn.execute('SELECT * FROM question WHERE id = ?', (question_id,)).fetchone()
    conn.close()
    if question is None:
        return jsonify({"message": "Question not found"}), 404
    return jsonify(dict(question)), 200

@app.route('/qset', methods=['POST'])
def add_qset():
    data = request.get_json()
    question_ids = ','.join(map(str, data['questions']))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO qset (questions) VALUES (?)",
        (question_ids,)
    )
    conn.commit()
    qset_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": qset_id, "message": "Question set added successfully"}), 201

@app.route('/qset', methods=['GET'])
def get_qset():
    qset_id = request.args.get('id')
    conn = get_db_connection()
    qset = conn.execute('SELECT * FROM qset WHERE id = ?', (qset_id,)).fetchone()
    conn.close()
    if qset is None:
        return jsonify({"message": "Question set not found"}), 404
    return jsonify(dict(qset)), 200

@app.route('/quiz', methods=['POST'])
def add_quiz():
    data = request.get_json()
    id_set = data['id_set']
    scores = data['scores']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO quiz (id_set, scores) VALUES (?, ?)",
        (id_set, ','.join(map(str, scores)))
    )
    conn.commit()
    quiz_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": quiz_id, "message": "Quiz added successfully"}), 201

@app.route('/quiz', methods=['GET'])
def get_quiz():
    quiz_id = request.args.get('id')
    conn = get_db_connection()
    quiz = conn.execute('SELECT * FROM quiz WHERE id = ?', (quiz_id,)).fetchone()
    conn.close()
    if quiz is None:
        return jsonify({"message": "Quiz not found"}), 404
    return jsonify(dict(quiz)), 200

if __name__ == '__main__':
    app.run(debug=True)

