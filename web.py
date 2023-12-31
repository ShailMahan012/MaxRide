#!/usr/bin/python3
from flask import Flask, render_template
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
domain = "maxrides.in"

@app.route("/")
def index():
    return render_template("index.html", domain=domain)


@app.route("/about")
def about():
    return render_template("about.html", domain=domain)


@app.route("/contact")
def contact():
    return render_template("contact.html", domain=domain)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

