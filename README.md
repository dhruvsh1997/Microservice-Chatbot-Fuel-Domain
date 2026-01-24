# Flask Chat WebSocket Service

A high-performance, real-time WebSocket chatbot specialized in the **Indian Fuel & Energy Sector**. Powered by **Flask-SocketIO** and the **Groq API** for ultra-fast inference.

---

## 🎯 Domain Specialization

This assistant is strictly optimized for the Indian energy landscape, covering:
- **Fossil Fuels:** Petroleum, diesel, petrol, kerosene, LPG, CNG, LNG.
- **Operations:** Refineries, upstream/downstream, city gas distribution.
- **Power:** Thermal, hydro, and renewable energy integration.
- **Market & Policy:** Fuel pricing, PSU operations (IOCL, BPCL, HPCL, ONGC, GAIL), PNGRB regulations, ethanol blending, and EV transition.

> [!IMPORTANT]  
> **Strict Domain Locking:** Any question outside the Indian fuel/energy sector will receive the standard response:  
> `the llm is configured for this specific domain question answering only.`

---

## 🛠️ Tech Stack

- **Backend:** Flask, Flask-SocketIO
- **LLM Inference:** Groq API (High-speed open-weight models)
- **Environment:** Python 3.10+
- **Containerization:** Docker

---

## 📂 Project Structure

```text
flask-chat-service/
├── app/
│   ├── __init__.py      # App factory
│   ├── config.py        # Configuration & Env management
│   ├── groq_client.py   # Groq API integration
│   ├── sockets.py       # WebSocket event logic
│   └── main.py          # Entry point
├── tests/               # Unit and integration tests
├── Dockerfile           # Container definition
├── requirements.txt     # Dependencies
└── .env.example         # Template for environment variables
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Groq API Key ([Get one here](https://console.groq.com/keys))

### Local Setup
1. **Clone & Navigate:**
   ```bash
   git clone <repo-url>
   cd flask-chat-service
   ```

2. **Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configuration:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

4. **Run:**
   ```bash
   python app/main.py
   ```
   The service will be available at `http://127.0.0.1:5000`.

### Docker Deployment
```bash
docker build -t flask-chat-service .
docker run --rm -p 5000:5000 --env-file .env flask-chat-service
```

---

## 🧪 Testing

Run the WebSocket client test suite:
```bash
python -m unittest tests/test_socket.py
```

---

## 📝 Usage Notes
- Connect via any Socket.IO client to the `/chat` namespace.
- Generic greetings (e.g., "Hi") are supported.
- Rate limits are governed by your Groq API tier.

