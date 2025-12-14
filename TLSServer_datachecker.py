import socket
import ssl

def create_ssl_context():
    """Create and configure SSL context with certificate."""
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('server.crt', 'server.key')
        return context
    except FileNotFoundError:
        print("Error: Certificate files not found. Run OpenSSL commands first.")
        return None
    except ssl.SSLError as e:
        print(f"SSL Error loading certificates: {e}")
        return None

def create_server_socket(ip, port):
    """Create and bind server socket."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen(1)
        return server_socket
    except socket.error as e:
        print(f"Socket Error: {e}")
        return None

def check_even_odd(number):
    """Check if number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

def handle_client(secure_conn, addr):
    """Handle communication with connected client."""
    print(f"Secure connection established with {addr}")
    try:
        while True:
            data = secure_conn.recv(1024).decode()
            if not data or data.lower() == "exit":
                print("Client disconnected.")
                break
            print(f"Received from client: {data}")
            try:
                number = int(data)
                response = check_even_odd(number)
            except ValueError:
                response = "Invalid input. Please enter a number."
            secure_conn.send(response.encode())
    except ssl.SSLError as e:
        print(f"SSL Error during communication: {e}")
    except socket.error as e:
        print(f"Socket Error during communication: {e}")
    finally:
        secure_conn.close()

def main():
    """Main function to run TLS server."""
    server_ip = "0.0.0.0"
    server_port = 13000
    
    # Create SSL context
    context = create_ssl_context()
    if context is None:
        return
    
    # Create server socket
    server_socket = create_server_socket(server_ip, server_port)
    if server_socket is None:
        return
    
    print(f"TLS server is listening on port {server_port}...")
    
    try:
        while True:
            conn, addr = server_socket.accept()
            try:
                secure_conn = context.wrap_socket(conn, server_side=True)
                handle_client(secure_conn, addr)
            except ssl.SSLError as e:
                print(f"SSL Handshake failed: {e}")
                conn.close()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
