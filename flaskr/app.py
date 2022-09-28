from threading import Lock
import socket

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
thread = None
thread_lock = Lock()


def background_thread():
    clientsocket = socket.socket()
    clientsocket.connect(("localhost", 35491))
    while True:
        random_number = clientsocket.recv(100).decode()
        socketio.emit('my_response',
                      {'random_number': random_number})


@app.route('/')
def index():
    return render_template('index.html')


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


if __name__ == "__main__":
    socketio.run(app)
