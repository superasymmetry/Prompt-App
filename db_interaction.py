import sqlite3
from pathlib import Path
import requests

def modify_user_input(title, content, input):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database WHERE title=? AND content=?",(title,content))
    row=c.fetchone()
    
    conn.close()

def get_prompt_info(title,content):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM database WHERE title=? AND content=?", (title,content))
    row = c.fetchone()
    conn.close()
    try:
        return row[2]
    except:
        return False
    
def add_prompt(tl, content):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    message = "Please engineer a prompt engineering prompt for ChatGPT. Please engineer the prompt based on the following:"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {
                "content": f"{message}:{tl}{content}",
                "role": "user"
            }
        ],
        "model": "gpt-4"
    }
    
    response = requests.post(url, json=data, headers=headers).json()
    completion_text = response['choices'][0]['message']['content']

    c.execute("INSERT INTO database (title, content, message) VALUES (?, ?, ?);",(tl, content,completion_text))
    conn.commit()
    conn.close()

    return True
