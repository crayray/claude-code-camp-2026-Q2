#!/usr/bin/env python3
"""Connect to tbaMUD, log in as the dummy player, and run commands.

Usage:
    python3 mud_client.py "look" "score" "exits"
"""
import socket
import sys

HOST = "localhost"
PORT = 4000
USERNAME = "dummy"
PASSWORD = "helloworld"


def recv_all(sock, wait=1.5):
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


def send_line(sock, line=""):
    sock.sendall((line + "\n").encode())


def login(sock):
    print(recv_all(sock, 2.0))  # welcome banner, asks for name
    send_line(sock, USERNAME)
    print(recv_all(sock, 1.5))  # asks for password
    send_line(sock, PASSWORD)
    print(recv_all(sock, 1.5))  # MOTD / "press return to continue"
    send_line(sock)  # bypass "PRESS RETURN" prompt
    print(recv_all(sock, 1.5))  # main menu (0-5)
    send_line(sock, "1")  # 1) Enter the game
    print(recv_all(sock, 1.5))


def main():
    commands = sys.argv[1:]
    sock = socket.create_connection((HOST, PORT))
    try:
        login(sock)
        for cmd in commands:
            send_line(sock, cmd)
            print(f">>> {cmd}")
            print(recv_all(sock, 1.5))
    finally:
        sock.close()


if __name__ == "__main__":
    main()
