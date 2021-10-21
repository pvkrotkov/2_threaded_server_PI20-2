import socket
from threading import Thread
import time
from progress.bar import IncrementalBar

N = 2**16 - 1

ports = []

def port_scanner(ps, pf):
    addr = "localhost"
    for port in range(ps, pf + 1):
        sock = socket.socket()
        try:
            print(port)
            sock.connect((addr, port))
            ports.append(port)
        except:
            continue
        finally:
            sock.close()

def main():
    bar = IncrementalBar('Countdown', max = N)

    a1 = Thread(target=port_scanner, args=[0, 13107])
    a2 = Thread(target=port_scanner, args=[13108, 26214])
    a3 = Thread(target=port_scanner, args=[26215, 39321])
    a4 = Thread(target=port_scanner, args=[39322, 52428])
    a5 = Thread(target=port_scanner, args=[52429, 65535])

    a1.start()
    a2.start()
    a3.start()
    a4.start()
    a5.start()

    for i in range(N):
        bar.next(n=5)
        time.sleep(1)

    bar.finish()

    a1.join()
    a2.join()
    a3.join()
    a4.join()
    a5.join()

    ports.sort()
    print(ports)

if __name__ == "__main__":
    main()