from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hi",methods=["GET"])
def hi():
    username = request.args.get("username", "unknown")
    return render_template("main.html", user=username)
