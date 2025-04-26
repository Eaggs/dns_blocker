import socket

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', 0))  # Bind na bilo koji slobodan port
        return s.getsockname()[1]

print(f"Free UDP port is: {find_free_port()}")
