"""Intentionally vulnerable demo app for a GitHub application security walkthrough.

Do not deploy. The SQL injection below is deliberate so CodeQL has something to find.
"""
import sqlite3

from flask import Flask, request

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute("INSERT INTO users (name, email) VALUES ('Ada', 'ada@example.com')")
    return conn


@app.route("/user")
def user():
    name = request.args.get("name", "")
    db = get_db()
   # Use a parameterized query to prevent SQL injection..
   rows = db.execute(
    "SELECT id, name, email FROM users WHERE name = ?",
    (name,)
).fetchall()
    return {"users": rows}


if __name__ == "__main__":
    app.run(debug=True)
