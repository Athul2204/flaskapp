from flask import Flask, render_template
import psycopg2


import os

DATABASE_URL = os.environ["DATABASE_URL"].strip()



app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("select * from users")
    data = cursor.fetchall()
    return render_template("index.html", data=data)


@app.route("/hello")
def hello():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(port=7000, debug=True)