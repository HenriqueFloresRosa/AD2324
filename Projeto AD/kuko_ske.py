import pickle
import threading
import net_server
import sock_utils
import kuko_data

class KukoSkeleton:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.net_server = net_server.Server(self.server_address, self.server_port, self.handle_client)
        print(f"Server listening on {self.server_address}:{self.server_port}")

    def start(self):
        self.net_server.start()

    def handle_client(self, conn):
        while True:
            data = sock_utils.receive_all(conn)
            if not data:
                break
            request = pickle.loads(data)
            response = self.process_request(request)
            serialized_response = pickle.dumps(response)
            sock_utils.send_all(conn, serialized_response)
        conn.close()

    def process_request(self, request):
        command_code = request[0]
        if command_code == 10:  # QUESTION
            question_text, options = request[1], request[2:-1]
            correct_option_index = request[-1]
            response = kuko_data.create_question(question_text, options, correct_option_index)
            if response:
                return [11, True, response]  # OK
            else:
                return [11, False]  # NOK
        elif command_code == 20:  # QSET
            quest_ids = request[1:]
            response = kuko_data.create_quest_set(quest_ids)
            if response:
                return [21, True, response]  # OK
            else:
                return [21, False]  # NOK
        elif command_code == 30:  # QUIZ
            id_set, *points = request[1:]
            response = kuko_data.create_quiz(id_set, *points)
            if response:
                return [31, True, response]  # OK
            else:
                return [31, False]  # NOK
        elif command_code == 40:  # LAUNCH
            quiz_id = request[1]
            response = kuko_data.start_quiz(quiz_id)
            if response == "OK":
                return [41, True]  # OK
            else:
                return [41, False]  # NOK
        elif command_code == 50:  # NEXT
            quiz_id = request[1]
            response = kuko_data.next_question(quiz_id)
            if response == "OK":
                return [51, True]  # OK
            else:
                return [51, False]  # NOK
        elif command_code == 60:  # REG
            quiz_id = request[1]
            response = kuko_data.register_participant(quiz_id)
            if response == "OK":
                return [61, True]  # OK
            else:
                return [61, False]  # NOK
        elif command_code == 70:  # GET
            quiz_id = request[1]
            response = kuko_data.get_current_question(quiz_id)
            if response:
                return [71, True] + response  # OK
            else:
                return [71, False]  # NOK
        elif command_code == 80:  # ANS
            quiz_id, answer_index = request[1:]
            response = kuko_data.answer_question(quiz_id, answer_index)
            if response == "OK":
                return [81, True]  # OK
            else:
                return [81, False]  # NOK
        elif command_code == 90:  # REL
            quiz_id = request[1]
            response = kuko_data.get_result(quiz_id)
            if response:
                return [91, True] + response  # OK
            else:
                return [91, False]  # NOK
        else:
            return [99, False]  # Código de comando inválido


