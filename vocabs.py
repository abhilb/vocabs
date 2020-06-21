import os
import requests
import random
import json
from flask import Flask, render_template, session, request
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
LAST_UPDATE = 'last_update'

def get_vocabs():
    vocab_txt = requests.get("https://raw.githubusercontent.com/abhilb/Notes/master/deutsch_vocabulary.md").text    
    vocabs = {}
    count = 0

    for line in vocab_txt.split('\n'):
        if line.startswith('#'):
            continue
        if not line:
            continue
        
        word, details = line.split(';')
        word = word.strip("* ")
        meaning, *examples = details.split('<br>')
        meaning = meaning.strip()

        example_arr = []
        for example in examples:
            de, *en = example.split('.')
            de = de.strip()
            if en: 
                en = en[0].strip('( )')
            example_arr.append({'de' : de, 'en' : en})
        word_info = {}
        word_info['meaning'] = meaning
        word_info['examples'] = example_arr
        count = count + 1
        vocabs[word] = word_info

    return vocabs

def get_next():
    vocab = get_vocabs()
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
    

@app.route("/einburgertest")
def einburgertest():
    return render_template("index.html", data=get_next())