import socket

sock = socket.socket()
host = input('Введите имя хоста: ')

if host == 'localhost':
    pass
else:
    if any(c.isalpha() for c in host) == True: # isalpha() - проверка на введенное имя хоста (все буквы)
        print('Введено некорректное имя хоста. По умолчанию выбран локальный хост')
        host = 'localhost'
    else:
        host_lst = host.split('.')
        for i in host_lst:
            if 0 <= int(i) <= 255:
                pass
            else:
                host = 'localhost'
                print('Введено некорректное имя хоста. По умолчанию выбран локальный хост')

try:
    port = int(input('Введите номер порта: '))
    if 0 <= port <= 65535:
        pass
    else:
        print('Введен некорректный номер порта. Номер порта по умолчанию 9090')
        port = 9090

except ValueError:
    print('Некорректный номер порта. Номер порта по умолчанию 9090')
    port = 9090

sock.connect((host, port))

while True:
    msg = input('Введите сообщение (для завершения работы с сервером напишите exit): ') # клиент вводит данные
    if msg == 'exit': 
        sock.send(msg.encode())
        print("Подключение прервано")
        break
    else:
        sock.send(msg.encode())
        data = sock.recv(1024)
        print("Полученные данные: ", data.decode())

sock.close()
