from flask import Flask
from views import views
import os

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

Path("database.db").touch()

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS database (id INTEGER PRIMARY KEY AUTOINCREMENT, title STRING, content TEXT, message TEXT);")

# An example prompt
# c.execute("INSERT INTO database (title, content, message) VALUES ('Translate', 'from English to Mandarin', 'Translate the following sentence from English to Mandarin.');")

conn.commit()
conn.close()

if __name__=="__main__":
  app.run(debug=True, port=8080)
