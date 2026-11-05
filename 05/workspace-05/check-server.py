import socket
import sys

def check_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, int(port)))
        print("Server up")
    except Exception:
        print("Server down")
    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Penggunaan: python check-server.py <host> <port>")
    else:
        check_server(sys.argv[1], sys.argv[2])