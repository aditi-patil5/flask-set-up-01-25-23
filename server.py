from flask import Flask, render_template, request, jsonify
import os

database_url = os.environ["DATABASE_URL"]
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hi",methods=["GET"])
def hi():
    username = request.args.get("username", "unknown")
    return render_template("main.html", user=username)

# api end point that returns a json
@app.route("/api/fact", methods=["GET"])
def api_fact():
    return jsonify({"id":17,"source":"brain", "content":"doritos exist"})


# Gets a json from a post request
@app.route("/api/fact", methods=["POST"])
def get_fact():
    print(request.json)
    return jsonify({"success":"ok"})