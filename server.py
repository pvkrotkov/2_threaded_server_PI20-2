import socket
from threading import Thread

sock = socket.socket()
sock.bind(('', 52429))
sock.listen(0)

users = []

def func():
	conn, addr = sock.accept()
	print(addr)
	users.append(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		for i in users:
			conn.sendto(data, (i))

		print(msg)

	conn.close()

def main():
	a1 = Thread(target=func)
	a2 = Thread(target=func)
	a3 = Thread(target=func)
	a1.start()
	a2.start()
	a3.start()


if __name__ == "__main__":
	main()
