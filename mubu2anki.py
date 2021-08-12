import opml
import os
import requests
import json
notes = []

def anki_post(notes):
    return requests.get('http://localhost:8765', data=json.dumps({
    "action": "addNotes",
    "params": {
        "notes": notes
    }
})).json()
    
    
def gen_anki(x):
    return {
                "deckName": deckName,
                "modelName": "Basic",
                "fields": {
                    "Front": x.text,
                    "Back": gen_note(x)
                }
            }
def gen_back(x):
    if len(x._note) > 0:
        return f'{x.text} ({x._note})'
    return x.text
def gen_note(a):
    ans = []
    for x in a:
        if x.text.endswith('?') or x.text.endswith('？'):
            notes.append(gen_anki(x))
        else:
            ans.append(gen_back(x))
            gen_note(x)
    return '<ol>' + ''.join([f'<li>{x}</li>' for x in ans]) + '</ol>'
def get_deck_name(file):
    try:
        return file[0][0][0].text
    except:
        return None
files = list(map(opml.parse, filter(lambda x: x.endswith('opml'), os.listdir())))
for file in files:
    deckName = get_deck_name(file)
    if deckName != None:
        gen_note(file)
    else:
        print('deckName not found')
print(anki_post(notes))