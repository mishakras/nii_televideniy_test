from threading import Lock
import socket

from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()


def background_thread():
    clientsocket = socket.socket()
    clientsocket.connect(("localhost", 35491))
    while True:
        data = clientsocket.recv(100).decode()
        print(data)
        socketio.emit('my_response',
                      {'data': data})


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
