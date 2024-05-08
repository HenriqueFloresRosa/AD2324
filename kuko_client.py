"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 14
Números de aluno: 56699 58618
"""



import sys
import requests

class KukoClient:
    def __init__(self, participant_id, server_address, server_port):
        self.participant_id = participant_id
        self.server_address = server_address
        self.server_port = server_port
        self.base_url = f"http://{self.server_address}:{self.server_port}"

    def start(self):
        while True:
            command = input("comando > ")
            if command == "EXIT":
                break
            else:
                self.process_command(command)
    
    def process_command(self, command):
        parts = command.split()
        command_code = parts[0]

        if command_code == "QUESTION":
            question_info = " ".join(parts[1:])
            response = self.send_question(question_info)
            print("Server response:", response)
        elif command_code == "QSET":
            qset_info = " ".join(parts[1:])
            response = self.send_qset(qset_info)
            print("Server response:", response)
        else:
            print("Invalid command")

    def send_question(self, question_info):
        url = f"{self.base_url}/question"
        payload = {"question_info": question_info}
        response = requests.post(url, json=payload)
        return response.json()

    def send_qset(self, qset_info):
        url = f"{self.base_url}/qset"
        payload = {"qset_info": qset_info}
        response = requests.post(url, json=payload)
        return response.json()


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kuko_client.py <participant_id> <server_address> <server_port>")
        sys.exit()

    participant_id = sys.argv[1]
    server_address = sys.argv[2]
    server_port = sys.argv[3]

    client = KukoClient(participant_id, server_address, server_port)
    client.start()

if __name__ == "__main__":
    main()
