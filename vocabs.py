import os
import requests
import random
import json
from flask import Flask, render_template, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

def get_next():
    vocab_txt = requests.get("https://raw.githubusercontent.com/abhilb/Notes/master/vocab.json").text
    vocab = json.loads(vocab_txt)
    count = len(vocab)
    idx = random.randint(0, count)
    data = {}
    while True:
        try:
            data['question'] = list(vocab.keys())[idx]
            data['answer'] = list(vocab.values())[idx]
        except IndexError:
            continue
        else:
            break
    return data

@app.route("/", methods=['GET', 'POST'])
def index():    
    return render_template("index.html", data=get_next())
    


