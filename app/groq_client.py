import requests
from app.config import Config
#Main Chat Inference
class GroqClient:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
    def get_response(self, message: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": [
                {"role": "system", "content": "You are an AI assistant specialized in the Indian Fuel Business or Working, including topics like fossil fuel, petroleum, gas, electricity, thermal, and related areas. You can respond to generic greetings such as 'hi' or 'hello'. For any questions outside this domain, respond exactly with: 'the llm is configured for this specific domain question answering only.' Do not answer or engage with any other topics."},
                {"role": "user", "content": message}
            ],
        }
        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]