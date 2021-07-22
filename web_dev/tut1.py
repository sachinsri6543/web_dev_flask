from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/human")
def hello_human():
    return "<p>Hello, Human Race!</p>"


app.run(debug=True)
