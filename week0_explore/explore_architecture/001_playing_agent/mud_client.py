import socket
import sys
import time

HOST = "localhost"
PORT = 4000


def recv_all(sock, wait=1.0):
    sock.settimeout(wait)
    data = b""
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
    except socket.timeout:
        pass
    return data.decode(errors="replace")


def send_line(sock, line):
    sock.sendall((line + "\n").encode())


def main():
    commands = sys.argv[1:]
    sock = socket.create_connection((HOST, PORT))
    print(recv_all(sock, 1.5))
    for cmd in commands:
        send_line(sock, cmd)
        print(f">>> {cmd}")
        print(recv_all(sock, 1.5))
    sock.close()


if __name__ == "__main__":
    main()
