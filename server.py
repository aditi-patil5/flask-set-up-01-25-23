from flask import Flask, render_template, request, jsonify, url_for,redirect, session
import os
import psycopg2
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth

# conn = psycopg2.connect(os.environ['DATABASE_URL'])
# conn.close()

# with conn.cursor as cur:
#     pass

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET"]

oauth = OAuth(app)  # oauth register with app
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)


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

#### Auth0 routes:
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)  # get a url from callback function
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    # edit the two lines below to customize to your website
    session["user"] = token         # set the session user to token
    session["uid"] = token["userinfo"]["sid"]
    session["email"] = token["userinfo"]["email"]
    session["picture"] = token["userinfo"]["picture"]
    return redirect("/")  # redirect to home /

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("hello_world", _external=True),  # may need to edit "hello_world" with function name
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )