from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Machine Learning API using Flask"

if __name__ == '__main__':
    app.run(debug=True)