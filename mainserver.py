import socket
import threading
import sys

sock = socket.socket()
sock.bind(('localhost', 7001))
sock.listen(3)
a = []

def Reciver():
     while 1:
         for i in range(len(a)):
             try:
                 data = a[i].recv(1024)
                 if data:
                     print(data.decode())
             except socket.error as e:
                 if e.errno == 10053:
                     a.pop(i)
                     print("Подключено пользователей:", len(a))
                 else:
                     raise

def Sender():
     while 1:
         global a
         message = input()
         if message:
             for i in range(len(a)):
                 a[i].send(message.encode())

def Accepter():
     while 1:
         global a
         a.append(sock.accept()[0])
         print("Подключено пользователй:", len(a))


 # init threads
t1 = threading.Thread(target=Reciver)
t2 = threading.Thread(target=Sender)
t3 = threading.Thread(target=Accepter)

 # start threads
t1.start()
t2.start()
t3.start()