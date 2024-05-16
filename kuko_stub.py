import pickle
import socket

class KukoStub:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def send_request(self, request_code, *args):
        request = [request_code] + list(args)
        serialized_request = pickle.dumps(request)
        return self.send_to_server(serialized_request)

    def send_to_server(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.server_address, self.server_port))
                sock.sendall(data)
                serialized_response = sock.recv(4096)
                return pickle.loads(serialized_response)
            except socket.error as e:
                print(f"Error communicating with server: {e}")

    def question(self, question_id, options):
        return self.send_request(10, question_id, options)

    def qset(self, *questions):
        return self.send_request(20, *questions)

    def quiz(self, quiz_id, *questions):
        return self.send_request(30, quiz_id, *questions)

    def launch(self, quiz_id):
        return self.send_request(40, quiz_id)

    def next(self, quiz_id):
        return self.send_request(50, quiz_id)

    def register(self, quiz_id):
        return self.send_request(60, quiz_id)

    def get_question(self, quiz_id):
        return self.send_request(70, quiz_id)

    def answer(self, quiz_id, answer, option_id):
        return self.send_request(80, quiz_id, answer, option_id)

    def get_result(self, quiz_id):
        return self.send_request(90, quiz_id)