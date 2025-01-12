from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/name/<string:fullName>")
def display_name(fullName):
    return {"fullName":f"{escape(fullName)}"}