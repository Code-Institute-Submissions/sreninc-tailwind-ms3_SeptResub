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
def generate():
    title = "Your Restaurant Booking Partner"
    return render_template("index.html", title=title)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
