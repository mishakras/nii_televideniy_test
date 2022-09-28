import random
import socket
import multiprocessing
import time


def gen():
    m = 0
    while True:
        m += 1
        yield m


def create_random_number(q, e):
    while True:
        random_number = random.randint(0, 100)
        print(random_number)
        q.put(random_number)
        e.set()
        time.sleep(1)


if __name__ == "__main__":
    random.seed()
    e = multiprocessing.Event()
    q = multiprocessing.Queue()
    w1 = multiprocessing.Process(name='random_number_generator',
                                 target=create_random_number,
                                 args=(q,e,))
    w1.start()
    serverSocket = socket.socket()
    ip = "127.0.0.1"
    port = 35491
    serverSocket.bind((ip, port))
    serverSocket.listen()
    while (True):
        (clientConnection, clientAddress) = serverSocket.accept()
        for _ in gen():
            e.wait()
            number = q.get()
            clientConnection.sendall(str.encode(str(number)))
