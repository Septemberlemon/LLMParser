import json
import requests


class OllamaLlm:
    def __init__(self, model_name, ollama_host="localhost:11434"):
        self.model_name = model_name
        self.ollama_host = ollama_host
        with open("prompt.txt", "r") as f:
            self.prompt = f.read()

    def get_response(self, file_path):
        with open(file_path, "r") as f:
            prompt = f.read() + self.prompt
        # print(prompt)

        payload = {
            "model": self.model_name,
            "system": "你是一个严格遵守提示词的ai助手",
            "prompt": prompt,
        }

        response = requests.post(
            "http://" + self.ollama_host + "/api/generate",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        full_response = ""

        for line in response.text.splitlines():
            chunk = json.loads(line)
            full_response += chunk["response"]
            if chunk["done"]:
                break

        return full_response
