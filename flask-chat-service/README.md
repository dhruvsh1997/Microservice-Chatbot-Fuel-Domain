# Flask Chat WebSocket Service

WebSocket-based chatbot service using Flask and GROQ API.

## Run Locally
```bash
pip install -r requirements.txt
python app/main.py


flask-chat-service/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── groq_client.py
│   ├── sockets.py
│   └── main.py
│
├── tests/
│   └── test_socket.py
│
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md
