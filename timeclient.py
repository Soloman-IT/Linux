import socket
from addtions import get_cli_data


def main():

    ip, port = get_cli_data()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    data  = client.recv(1024)
    print(data.decode())  



if __name__ == "__main__":
    main()