import random
import socket
import multiprocessing
import time


def gen():
    m = 0
    while True:
        m += 1
        yield m


def create_random_number(q, e1, e2):
    while True:
        random_number = random.randint(0, 100)
        print(random_number)
        if e2.is_set():
            q.put(random_number)
        e1.set()
        time.sleep(1)


if __name__ == "__main__":
    random.seed()
    e1 = multiprocessing.Event()
    e2 = multiprocessing.Event()
    q = multiprocessing.Queue()
    w1 = multiprocessing.Process(name='random_number_generator',
                                 target=create_random_number,
                                 args=(q,e1, e2))
    w1.start()
    serverSocket = socket.socket()
    ip = "127.0.0.1"
    port = 35491
    serverSocket.bind((ip, port))
    serverSocket.listen()
    while (True):
        (clientConnection, clientAddress) = serverSocket.accept()
        e2.set()
        for _ in gen():
            e1.wait()
            number = q.get()
            try:
                clientConnection.sendall(str.encode(str(number)))
            except:
                e2.clear()
                break
