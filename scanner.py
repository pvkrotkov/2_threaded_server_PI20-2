import socket
import threading

N = 2**16 - 1
counter = 0
spaces = " " * 100 + "\n"


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)

    if iteration == total:
        print()


def scan(arr, thr, host):
    global counter
    for port in arr:
        sock = socket.socket()
        try:
            sock.connect((host, port))
            print("Port", port, "open", end=spaces)
            printProgressBar(counter, 66, prefix='Progress:', suffix='Success', length=50)
        except:
            continue
        finally:
            sock.close()
    counter += 1
    return


host = input("Host:")
if host == '':
    host = '127.0.0.1'

printProgressBar(0, 66, prefix='Progress:', suffix='Success', length=50)

for thread in range(66):
    arr = []
    for i in range(1000):
        arr.append(thread * 1000 + i)
        if arr[i] >= N:
            break
    thr = threading.Thread(target=scan, args=[arr, thread, host])
    thr.start()
