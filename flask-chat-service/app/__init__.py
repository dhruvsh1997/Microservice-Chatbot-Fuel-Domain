from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(
    cors_allowed_origins="*",
    async_mode="threading",  # important for Windows
)


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    socketio.init_app(app)

    # Import socket handlers AFTER init
    from app import sockets  # noqa: F401

    return app
