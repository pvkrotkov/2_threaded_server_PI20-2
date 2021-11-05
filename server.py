import socket
import threading


def proc_client(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data)


add = ('', 9090)


sock = socket.socket()
sock.bind(add)
sock.listen()
print('Начало прослушивания порта', add[1])

while True:
	conn, addr = sock.accept()
	thread = threading.Thread(target=proc_client, args=[conn])
	thread.start()