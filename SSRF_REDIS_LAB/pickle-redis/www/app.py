#!/usr/bin/env python2

from flask import Flask, render_template, request, redirect, url_for, session
import httplib
import urllib
import urlparse

from session_redis import RedisSessionInterface

app = Flask(__name__)
app.session_interface = RedisSessionInterface()

@app.route("/", methods=["GET","POST"])
def index():

    result = ""
    if not session.get("username"):
        return redirect(url_for("login"))

    if request.method == "POST":
        url = request.form.get("url")
        result = fetch(url)
    return render_template("index.html", context = {"result" : result, "username" : session.get("username")})

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        session["username"] = request.form.get("username", "Guest")

        return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username")

    return redirect(url_for("login"))

def fetch(url):
    url = urlparse.urlsplit(url)
    # httplib is vulnerable to CRLF Injection
    h = httplib.HTTPConnection(url.netloc)
    h.request("GET", str(urllib.unquote(url.path)))
    response = h.getresponse()
    data = response.read()
    h.close()

    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3333)