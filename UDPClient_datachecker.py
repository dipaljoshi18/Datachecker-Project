import socket

server_ip = "127.0.0.1"
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a number (or 'exit' to quit): ")
    client_socket.sendto(message.encode(), (server_ip, server_port))

    if message.lower() == "exit":
        print("Closing client...")
        break

    data, server_address = client_socket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")

client_socket.close()
