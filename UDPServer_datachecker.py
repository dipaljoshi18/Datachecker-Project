import socket

server_ip = "127.0.0.1"
server_port = 12000
buffer_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))
print("UDP server is ready to receive messages...")

while True:
    data, client_address = server_socket.recvfrom(buffer_size)
    message = data.decode()
    print(f"Received from client: {message}")

    if message.lower() == "exit":
        print("Closing server...")
        break

    try:
        number = int(message)
        response = f"{number} is even" if number % 2 == 0 else f"{number} is odd"
    except ValueError:
        response = "Invalid input. Please send a number."

    server_socket.sendto(response.encode(), client_address)

server_socket.close()
