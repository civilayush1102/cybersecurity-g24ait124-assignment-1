import socket
import math

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

data = client_socket.recv(1024).decode()
print("Received from Server:", data)

try:
    num = float(data)
    result = math.sqrt(num)
except:
    result = "Invalid number"

client_socket.send(str(result).encode())
print("Sent result back to server:", result)

client_socket.close()
