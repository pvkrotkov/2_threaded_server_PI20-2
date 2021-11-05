import socket
import threading
import queue
import sys
import shutil
from time import sleep

columns = shutil.get_terminal_size().columns
checked = 0
lock = threading.RLock()


def progress_bar() -> None:
    global checked
    while checked < 65535:
        pr = (checked + 1) / 65535
        # возврат каретки с вывоводом прогресс-бара
        sys.stdout.write('\r' + "*" * int(pr * 10) + f" {pr * 100:.0f}%")
        sys.stdout.flush()
        sleep(0.0001)
    print()


def scanner(host: str, num: int, que: queue.Queue) -> None:
    global checked

    g = num
    while (num != g + 555) and num < 65536:
        try:

            scan = socket.socket()
            scan.connect((host, num))
            que.put(num)

        except OSError:
            pass

        finally:
            num += 1
            scan.close()
            try:
                lock.acquire()
                checked += 1

            finally:
                lock.release()


if __name__ == "__main__":

    port = 562 # количество обрабатываемых каждым потоком портов
    NUM = 120
    num_port = 1
    threads = []


    scan = socket.socket()

    host_name = input("введите имя хоста ") or 'localhost'
    que = queue.Queue()  # открытые порты
    bar = threading.Thread(target=progress_bar)
    bar.start()
    for i in range(NUM):
        new_thread = threading.Thread(target=scanner, args=[host_name, port, que])
        threads.append(new_thread)
        new_thread.start()
        port += 546  # каждый следующий поток рассматривает на 546 больше

    for thread in threads:
        thread.join()
    bar.join()

    ports = []
    while not que.empty():
        ports.append(que.get())
    print("Свободные порты: ", end='')
    print(*sorted(ports), sep='; ')
