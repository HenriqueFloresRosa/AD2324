#para testar o kuko_data.py
from kuko_data import KUKO
kd = KUKO('kuko.db')

while (1):
    user_input = input('comando >').strip()
    cmd = user_input.split(';')
    try:
        match cmd[0]:
            case "QUESTION":
                question = cmd[1]
                answer = cmd[2:-1]
                k = int(cmd[-1])
                print('nova pergunta:', kd.add_quest(question, answer, k))
            case "QSet":
                quest_ids = [int(a) for a in cmd[1:]]
                print('novo Qset:', kd.add_quest_set(quest_ids))
            case "QUIZ":
                quest_ids = [int(cmd[1])]
                points =[int(a) for a in cmd[2:]]
                print('novo QUIZ:', kd.add_quiz(quest_ids, points))
    except Exception as e:
        print("ERRO:", e)