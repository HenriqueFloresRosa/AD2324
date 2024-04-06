"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 14
Números de aluno: 56699 58618
"""
import sys
from net_client import NetClient

class KukoClient:
    def __init__(self, participant_id, server_address, server_port):
        self.participant_id = participant_id
        self.server_address = server_address
        self.server_port = server_port
        self.client = NetClient(self.server_address, self.server_port)

    def start(self):
        self.client.connect_to_server()
        while True:
            command = input("comando > ")
            if command == "EXIT":
                self.client.close_connection()
                break
            else:
                self.process_command(command)

    def process_command(self, command):
        parts = command.split(";")
        command_code = parts[0]

        if command_code == "QUESTION":
            question_id, options = parts[1], parts[2:]
            response = self.client.send_message_to_server([10, question_id, options])

        elif command_code == "QSET":
            questions = parts[1:]
            response = self.client.send_message_to_server([20] + questions)

        elif command_code == "QUIZ":
            quiz_id, questions = parts[1], parts[2:]
            response = self.client.send_message_to_server([30, quiz_id] + questions)

        elif command_code == "LAUNCH":
            quiz_id = parts[1]
            response = self.client.send_message_to_server([40, quiz_id])

        elif command_code == "NEXT":
            quiz_id = parts[1]
            response = self.client.send_message_to_server([50, quiz_id])

        elif command_code == "REG":
            quiz_id = parts[1]
            response = self.client.send_message_to_server([60, quiz_id])

        elif command_code == "GET":
            quiz_id = parts[1]
            response = self.client.send_message_to_server([70, quiz_id])

        elif command_code == "ANS":
            quiz_id, answer, option_id = parts[1:]
            response = self.client.send_message_to_server([80, quiz_id, answer, option_id])

        elif command_code == "REL":
            quiz_id = parts[1]
            response = self.client.send_message_to_server([90, quiz_id])

        else:
            print("Comando inválido")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kuko_client.py <participant_id> <server_address> <server_port>")
        sys.exit(1)

    participant_id = sys.argv[1]
    server_address = sys.argv[2]
    server_port = int(sys.argv[3])

    client = KukoClient(participant_id, server_address, server_port)
    client.start()

if __name__ == "__main__":
    main()

