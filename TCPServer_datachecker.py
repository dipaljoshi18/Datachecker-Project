import socket

server_ip = "127.0.0.1"
server_port = 13000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("TCP server is listening...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    data = conn.recv(1024).decode()
    print("Received from client:", data)  # <-- Add this line!
    if not data or data.lower() == "exit":
        print("Connection closed.")
        break
    try:
        number = int(data)
        response = f"{number} is even" if number % 2 == 0 else f"{number} is odd"
    except ValueError:
        response = "Invalid input."
    conn.send(response.encode())

conn.close()
server_socket.close()
