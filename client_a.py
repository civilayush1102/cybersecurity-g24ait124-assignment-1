import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

number = input("Enter a number to send: ")
start_time = time.time()
client_socket.send(number.encode())

result = client_socket.recv(1024).decode()
end_time = time.time()

print("Result received:", result)
print(f"Round-trip delay: {end_time - start_time:.5f} seconds")

client_socket.close()
