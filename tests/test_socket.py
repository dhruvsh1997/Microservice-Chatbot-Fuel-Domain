import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected")
    sio.emit("chat_message", {"message": "Hello, who are you?"})

@sio.on("message")
def on_message(data):
    print("Received:", data)

sio.connect("http://localhost:8002")
sio.wait()
