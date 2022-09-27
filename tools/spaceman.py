import json
import requests


def humans():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    text = response.text
    ready_text = json.loads(text)
    return ready_text
