import requests
import json
import pprint
def anki_ls():
    return requests.get('http://localhost:8765', data=json.dumps({
      "action": "deckNames"
})).json()
pprint.pprint(anki_ls())