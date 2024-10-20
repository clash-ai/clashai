__version__ = "1.0.6"

import requests
import os

class Client:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key if api_key else os.getenv("CLASHAI_API_KEY")
        self.base_url = base_url if base_url else "https://clashai.eu/"
        self.chat = Chat(self.api_key, self.base_url)

class Chat:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.completions = Completions(api_key, base_url)

class Completions:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key if api_key else os.getenv("CLASHAI_API_KEY")
        self.base_url = base_url if base_url else "https://clashai.eu/"

    def create(self, messages: list, model: str = "chatgpt-4o-latest"):
        api_key = self.api_key
        endpoint = "v1/chat/completions"
        url = f"{self.base_url}/{endpoint}"
        payload = {
            "model": model,
            "messages": messages,
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
