from flask import Flask, request, render_template, sessions
from processing import calculation

app = Flask(__name__)

@app.route('/', )
def hello_world():
    render_template("form.html")