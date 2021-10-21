import socket
from time import sleep

def main():
    #основа клиента
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect(('localhost', 9090))

    while True:
        msg = input()
        if(msg == "exit"):
            break
            #Проверка выхода
        sock.send(msg.encode())
        data = sock.recv(1024)
        print(data.decode())

    sock.close()

if __name__ == "__main__":
    main();    
