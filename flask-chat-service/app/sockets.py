from flask_socketio import emit
from app import socketio
from app.groq_client import GroqClient

groq_client = GroqClient()


@socketio.on("connect")
def handle_connect():
    emit("message", {"data": "Connected to Chatbot"})


@socketio.on("chat_message")
def handle_chat_message(data):
    user_message = data.get("message")

    if not user_message:
        emit("error", {"error": "Message is required"})
        return
    try:
        response = groq_client.get_response(user_message)
        emit("chat_response", {"message": response})
    except Exception as e:
        emit("error", {"error": str(e)})
