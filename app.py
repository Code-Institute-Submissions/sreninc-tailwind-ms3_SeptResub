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
    header = {
        "title": "Reservations",
        "titleGreen": "made easy",
        "subTitle": "Manage your operations in one place and get guests when you need them most.",
        "displayButtons": "yes"
    }
    return render_template("index.html", title=title, header=header)


@app.route("/features")
def features():
    title = "Features To Grow Your Restaurant"
    header = {
        "title": "Features",
        "titleGreen": "for growth",
        "subTitle": "Booking and guest management made to help you grow your restaurant.",
        "displayButtons": "yes"
    }
    return render_template("features.html", title=title, header=header)


@app.route("/contact")
def contact():
    title = "Contact Us To Discuss Your Restaurants Needs"
    header = {
        "title": "Need Help?",
        "titleGreen": "We're here.",
        "subTitle": "Let us answer your questions and guide you in the right direction.",
        "displayButtons": "no"
    }
    return render_template("contact.html", title=title, header=header)


@app.route("/signup")
def signup():
    title = "Signup And Grow Your Restaurant"
    header = {
        "title": "On your way",
        "titleGreen": "to growth",
        "subTitle": "Choose the package that suits your restaurant and let's get started!",
        "displayButtons": "no"
    }
    return render_template("signup.html", title=title, header=header)


@app.route("/login")
def login():
    title = "Login To Your Account"
    header = {
        "title": "Welcome",
        "titleGreen": "back home",
        "subTitle": "We're glad you are back.",
        "displayButtons": "no"
    }
    return render_template("login.html", title=title, header=header)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
