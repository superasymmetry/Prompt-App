from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from db_interaction import get_prompt_info, add_prompt
import requests
import os
import json
import sqlite3
# import pycurl
from pathlib import Path
from urllib.parse import urlencode
import json

views = Blueprint(__name__, "views")

@views.route('/', methods=['GET','POST'])
def home():
    if request.method=="POST":
        title = request.form["title"]
        description = request.form["des"]
        print(title, description)
        add_prompt(title, description)
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM database")
        records = c.fetchall()
        conn.close()
        records2=[]
        for i in records:
            temp = []
            for j, a in enumerate(i):
                if j<2:
                    temp.append(a)
            records2.append(temp)
        return render_template('index.html', rows=records2)

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database")
    records = c.fetchall()
    conn.close()
    records2=[]
    for i in records:
        temp = []
        for j, a in enumerate(i):
            if j>0 and j<3:
                temp.append(a)
        records2.append(temp)
    return render_template("index.html", rows=records2)
# def Display_IMG():
#     Flask_Logo = os.path.join(app.config['UPLOAD_FOLDER'], 'flask-logo.png')
#     return render_template("index.html", user_image=Flask_Logo)


@views.route('/prompt', methods = ['GET', 'POST'])
def prompt():
    if request.method == "POST":
        pt = request.form["pr"]
        clicked_item = request.args.get('item')
        content = request.args.get('content')
        message = get_prompt_info(clicked_item,content)
        # message = 'Translate the following from English to Mandarin:'
        url = "https://api.openai.com/v1/chat/completions"
        with open(r'C:\Users\2025130\Downloads\Prompt-Library-main\Prompt-Library-main\config.json') as config_file:
            config = json.load(config_file)

        api_key = config['api_key']
        headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }
        data = {
            "messages": [
                {
                    "content": f"{message}:{pt}",
                    "role": "user"
                }
            ],
            "model": "gpt-4"
        }
        
        
        response = requests.post(url, json=data, headers=headers).json()
        completion_text = response['choices'][0]['message']['content']

        # c=pycurl.Curl()
        # c.setopt(c.URL, 'https://api.openai.com/v1/chat/completions')
        # post_data = {'field': 'value'}
        return render_template('form_page.html', response1=completion_text)
    else:
        return render_template("form_page.html")
