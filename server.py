# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(2)

print("Server is waiting for connections...")

client_a, addr_a = server_socket.accept()
print("Connected with Client A:", addr_a)

client_b, addr_b = server_socket.accept()
print("Connected with Client B:", addr_b)

data = client_a.recv(1024).decode()
print("Received from Client A:", data)

client_b.send(data.encode())
print("Sent to Client B")

result = client_b.recv(1024).decode()
print("Received result from Client B:", result)

client_a.send(result.encode())
print("Result sent back to Client A")

client_a.close()
client_b.close()
server_socket.close()
