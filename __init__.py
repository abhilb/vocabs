import os
import requests
import random
import json
from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    vocab_txt = requests.get("https://raw.githubusercontent.com/abhilb/Notes/master/vocab.json").text
    
    print(vocab_txt)

    vocab = json.loads(vocab_txt)
    count = len(vocab)
    idx = random.randint(0, count)
    data = {}
    data['question'] = list(vocab.keys())[idx]
    data['answer'] = list(vocab.values())[idx][0]
    if request.method == 'POST':
        return render_template("index.html", data=data)
    else:
        return render_template("index.html", data=data)

