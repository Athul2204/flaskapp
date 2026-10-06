from flask import Flask, render_template
import psycopg2

DATABASE_URL = "postgresql://sample_db_2doe_user:CPOVijMTS5wvXuFy6DZtMSLwBoEJBqTq@dpg-db29i1bbc2fs73fpqa7g-a/sample_db_2doe"


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