from requests import Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def sendmsg(msg):

    BASE_URL = "https://graph.facebook.com/"
    API_VERSION = "v13.0/"
    SENDER = "103711299074871/"
    ENDPOINT = "messages/"
    URL = BASE_URL + API_VERSION + SENDER + ENDPOINT
    API_TOKEN = "EAAHv7hbPujkBALIJp5ta7VZANIn3RRJNsZBbdPTavCx8DGtAFnAcubdhZBDbafSqRYhiUp3NSpIeQLQwHnm4s2yqAh4gywnuVDZA0IRbxvDONZB37eV826HGLYqFAjOcHC3oXWMErhQkLBgpZAoDr3z0H6S7yf0ZARgp8KFb2qjryigZAJ9jVEfai9JKY3PXksasRQHXtwWFyAZDZD"
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
