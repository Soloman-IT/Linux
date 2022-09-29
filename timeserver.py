import socket
from addtions import get_cli_data
import datetime


def main():
    ip, port = get_cli_data()

    server = socket.socket()
    server.bind((ip, port))
    while True:
        server.listen()
        conn, addr = server.accept()
        data = datetime.datetime.now()

        conn.send(f"{data.year}-{data.month}-{data.day} {data.hour}:{data.minute}".encode("utf-8"))
        conn.close()


if __name__ == "__main__":
    main()