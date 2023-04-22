from flask import Flask, render_template, request
from chatbot import predict_class, get_response
import json
# import request

app = Flask(__name__)

intents = json.loads(open("intents.json").read())


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/output', methods=['POST'])
def chatbot():
    message = request.form.get("message")
    print(message)
    ints = predict_class(message)
    res = get_response(ints, intents)

    return render_template("index.html", result=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
