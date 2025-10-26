import socket

server_ip = "127.0.0.1"
server_port = 13000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Connected to the TCP server.")

while True:
    message = input("Enter a number (or 'exit' to quit): ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

client_socket.close()
