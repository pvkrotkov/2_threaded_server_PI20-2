import socket
import threading

ports = []
for i in range (0, 1000):
    ports.append(0)

def open (port):
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        sock.connect(('www.mail.ru', port))
    except:
        sock.close()
    else:
        ports[port] = 1
        sock.close()


t = [threading.Thread(target=open, args=[i]) for i in range(1, 1000)]
[t1.start() for t1 in t]


[t1.join() for t1 in t]
for i in range (0, 1000):
    if ports[i] == 1:
        print ("Port ", i + 1, "opened")
