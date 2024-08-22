from flask import Flask

app = Flask(__name__)


@app.route("/index")
def hello():
    return "Hello World"


@app.route("/greet/<str:param>/")
def greet(param):
    return "Hello Mr/Mrs " + param


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=8000)
