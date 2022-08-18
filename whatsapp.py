from requests import Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def sendmsg(msg):

    BASE_URL = "https://graph.facebook.com/"
    API_VERSION = "v13.0/"
    SENDER = "103711299074871/"
    ENDPOINT = "messages/"
    URL = BASE_URL + API_VERSION + SENDER + ENDPOINT
    API_TOKEN = "EAAHv7hbPujkBACjoQuZAJp1JD0ZBlCnKGKpRVIjjD8ZBjMFT0VSnfRUNx3nZB7eutB14KqCAPrGWZAf3yRecrTxCJu2lc4LlqWBBIkPwZCf9k8Y4nFB9XjUmZA9npnBXj3HZAhzDXtJuF2kdZAQAX12CI0cZAF0lCtw4r5Io2MrZAmUFve2waIFCBosAWDhS5J1G66fO2tVBnSM2wZDZD"
    TO = "263774405106"
    headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
    }
    parameters = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": TO,
        "type": "text",
        "text": {
        "preview_url": "false",
        "body": msg
        }
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.post(URL, json=parameters)
        data = json.loads(response.text)
        print(f"data: {data}")
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
