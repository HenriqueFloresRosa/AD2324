"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Grupo: 14
Números de aluno: 56699 XXXXX
"""

def create_tcp_server_socket(address, port, queue_size=1):
  
    
  server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

  
  server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

  try:
    server_socket.bind((address, port))
    server_socket.listen(queue_size)
    return server_socket
  except OSError as e:
    raise OSError(f"Failed to create TCP server socket: {e}")

def create_tcp_client_socket(address, port):
  client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

  try:
    client_socket.connect((address, port))
    return client_socket
  except OSError as e:
    raise OSError(f"Failed to create TCP client socket: {e}")
    

