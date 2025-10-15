import Model.globals as globals
import requests


def obtenerRespuestaPrompt(request):
    messages = [{"role": "user", "content": request}]
    payload = {"model": "Goosedev/luna", "messages": messages, "stream": False}
    resp = requests.post(f"http://{globals.ip}:11434/api/chat", json=payload)
    data = resp.json()
    return data["message"]["content"]



