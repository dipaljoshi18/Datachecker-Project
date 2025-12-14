import socket
import ssl

def create_ssl_context():
    """Create and configure SSL context for client."""
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations('server.crt')
        return context
    except FileNotFoundError:
        print("Error: server.crt not found. Copy it from the server.")
        return None
    except ssl.SSLError as e:
        print(f"SSL Error loading certificate: {e}")
        return None

def connect_to_server(context, server_ip, server_port):
    """Establish secure connection to server."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_socket = context.wrap_socket(client_socket, server_hostname=server_ip)
        secure_socket.connect((server_ip, server_port))
        return secure_socket
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
        return None
    except socket.error as e:
        print(f"Connection Error: {e}")
        return None

def communicate(secure_socket):
    """Handle communication with server."""
    try:
        while True:
            message = input("Enter a number (or 'exit' to quit): ")
            secure_socket.send(message.encode())
            if message.lower() == "exit":
                print("Disconnecting...")
                break
            response = secure_socket.recv(1024).decode()
            print(f"Received from server: {response}")
    except ssl.SSLError as e:
        print(f"SSL Error during communication: {e}")
    except socket.error as e:
        print(f"Socket Error during communication: {e}")
    except KeyboardInterrupt:
        print("\nDisconnecting...")

def main():
    """Main function to run TLS client."""
    server_ip = "10.0.0.111"  # Change to your server's IP
    server_port = 13000
    
    # Create SSL context
    context = create_ssl_context()
    if context is None:
        return
    
    # Connect to server
    secure_socket = connect_to_server(context, server_ip, server_port)
    if secure_socket is None:
        return
    
    print("Connected to the TLS server.")
    
    try:
        communicate(secure_socket)
    finally:
        secure_socket.close()

if __name__ == "__main__":
    main()
