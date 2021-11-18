import socket
import threading

isOpen = [0]*3000
checked = [0]*3000

def open (port):
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        sock.connect(('www.yandex.ru', port))
    except:
        sock.close()
        checked[port] = 1
    else:
        isOpen[port] = checked[port] = 1
        sock.close()


t = [threading.Thread(target=open, args=[i]) for i in range(1, 3000)]
[t1.start() for t1 in t]

a = 0
while a  < 2999:
    a = sum(checked)
    print (str(a) + " of 2999")
    
[t1.join() for t1 in t]

for i in range (0, 3000):
    if isOpen[i] == 1:
        print ("Port", i + 1, "is opened")
    else:
        print ("Port", i + 1, "is not opened")
