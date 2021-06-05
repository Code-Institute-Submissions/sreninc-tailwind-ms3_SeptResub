import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_assets import Bundle, Environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

assets = Environment(app)
css = Bundle("css/main-dev.css", output="css/main.css", filters="postcss")

assets.register("css", css)
css.build()


@app.route("/")
@app.route("/index")
def index():
    title = "Your Restaurant Booking Partner"
    return render_template("index.html", title=title)


@app.route("/features")
def features():
    title = "Features To Grow Your Restaurant"
    return render_template("features.html", title=title)


@app.route("/contact")
def contact():
    title = "Contact Us To Discuss Your Restaurants Needs"
    return render_template("contact.html", title=title)


@app.route("/signup")
def signup():
    title = "Signup And Grow Your Restaurant"
    return render_template("signup.html", title=title)


@app.route("/login")
def login():
    title = "Login To Your Account"
    return render_template("login.html", title=title)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
