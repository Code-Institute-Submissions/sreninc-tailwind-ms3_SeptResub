import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_assets import Bundle, Environment
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


assets = Environment(app)
css = Bundle("css/main-dev.css", output="css/main.css", filters="postcss")

assets.register("css", css)
css.build()

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

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


@app.route("/dashboard")
def dashboard():
    title = "Dashboard"
    bookings = list(mongo.db.bookings.find())
    guests = list(mongo.db.clients.find())
    total_guests = len(guests)
    total_bookings = len(bookings)
    total_sales = 0
    no_show_percentage = 0
    completed_percentage = 0
    avg_booking_value = 0
    for booking in bookings:
        print(booking["status"])
    for booking in bookings:
        if booking["status"] == "completed":
            completed_percentage += 1
            total_sales += int(booking["value"])
        elif booking["status"] == "no-show":
            no_show_percentage += 1
    avg_booking_value = int(total_sales / completed_percentage)
    total_sales = int(total_sales)
    completed_percentage = int((completed_percentage / total_bookings) * 100)
    no_show_percentage = int((no_show_percentage / total_bookings) * 100)

    stats = {
        "total_guests": total_guests,
        "total_bookings": total_bookings,
        "total_sales": total_sales,
        "no_show_percentage": no_show_percentage,
        "completed_percentage": completed_percentage,
        "avg_booking_value": avg_booking_value
    }
    return render_template("dashboard.html", title=title, stats=stats)


@app.route("/team")
def team():
    title = "Team"
    account = mongo.db.users.find_one(
        {"email": "sreninc@gmail.com"})["account"]
    admin = mongo.db.users.find_one(
        {"email": "sreninc@gmail.com"}
    )["access"]
    if admin == "admin":
        admin = "true"
    else:
        admin = "false"

    team = list(mongo.db.users.find({
        "account": account
    }))

    return render_template("team.html", team=team, admin=admin, title=title)


@app.route("/guests")
def guests():
    title = "Guests"
    guests = list(mongo.db.clients.find())
    for x in range(len(guests)):
        guests[x]["rating"] = int(guests[x]["rating"])
    pages = int(math.ceil(len(guests) / 50))
    current_page = 1
    return render_template("guests.html", guests=guests, title=title, pages=pages, current_page=current_page)


@app.route("/guest/<id>")
def guest(id):
    guest = mongo.db.clients.find_one(
            {"_id": ObjectId(id)})
    guest["rating"] = int(guest["rating"])
    bookings = list(mongo.db.bookings.find(
        {"client_id": id}))
    title = guest["first_name"] + " " + guest["last_name"]

    for x in range(len(bookings)):
        written_date = datetime.strptime(bookings[x]["date"], '%Y-%m-%d')
        bookings[x]["written_date"] = written_date.strftime("%a %d %b")
        bookings[x]["full_name"] = guest["first_name"] + " " + guest["last_name"]
        bookings[x]["rating"] = int(bookings[x]["rating"])
    return render_template("guest-detail.html", guest=guest, bookings=bookings, title=title)

@app.route("/bookings")
@app.route("/bookings/date/<date>/status/<status>")
def bookings(date="", status=""):
    title = "Bookings"
    if len(date) == 0:
        date = datetime.today().strftime('%Y-%m-%d')
    if status == "all":
        status = ""

    if date and status:
        bookings = list(mongo.db.bookings.find(
            {
                "status": status,
                "date": date
            }
        ))
    elif date:
        bookings = list(mongo.db.bookings.find(
            {
                "date": date
            }
        ))
    elif status:
                bookings = list(mongo.db.bookings.find(
            {
                "status": status
            }
        ))
    else:
        bookings = list(mongo.db.bookings.find())

    clients = list(mongo.db.clients.find(
        {},
        {"first_name": 1, "last_name": 1}))
    for x in range(len(bookings)):
        written_date = datetime.strptime(bookings[x]["date"], '%Y-%m-%d')
        bookings[x]["written_date"] = written_date.strftime("%a %d %b")
        bookings[x]["rating"] = int(bookings[x]["rating"])

        for y in range(len(clients)):
            if str(clients[y]["_id"]) == str(bookings[x]["client_id"]):
                bookings[x]["full_name"] = clients[y]["first_name"] + " " + clients[y]["last_name"]
        
    return render_template("bookings.html", bookings=bookings, title=title, date=date, status=status)


@app.route("/booking/<id>", methods=["GET", "POST"])
def booking(id):
    booking = mongo.db.bookings.find_one(
            {"_id": ObjectId(id)})

    guest = mongo.db.clients.find_one(
            {"_id": ObjectId(booking["client_id"])})
    booking["rating"] = int(booking["rating"])
    title = "Booking For: " + guest["first_name"] + " " + guest["last_name"]

    written_date = datetime.strptime(booking["date"], '%Y-%m-%d')
    booking["written_date"] = written_date.strftime("%a %d %b")
    booking["full_name"] = guest["first_name"] + " " + guest["last_name"]
    booking["rating"] = int(booking["rating"])
    return render_template("booking-detail.html", guest=guest, booking=booking, title=title)


@app.route("/update_booking/<id>", methods=["GET", "POST"])
def update_booking(id):
    if request.method == "POST":
        booking = mongo.db.bookings.find_one(
            {"_id": ObjectId(id)})
        booking_id = booking["_id"]

        guest = mongo.db.clients.find_one(
            {"_id": ObjectId(booking["client_id"])})

        if request.form.get("notes_service"):
            mongo.db.clients.update_one(
                {"_id": ObjectId(guest["_id"])},
                {"$set": {
                    "notes_service": request.form.get("notes_service"),
                    "notes_kitchen": request.form.get("notes_kitchen"),
                    "notes_allergies": request.form.get("notes_allergies")
                    }
                }
            )
        else:
            mongo.db.bookings.update(
                {"_id": ObjectId(id)},
                {"$set": {
                    "date": request.form.get("date"),
                    "time": request.form.get("time"),
                    "people": request.form.get("people"),
                    "status": request.form.get("status"),
                    "value": request.form.get("value"),
                    "updated_by": "sreninc@gmail.com",
                    "updated_date": datetime.today()
                    }
                }
            )
            
            return redirect(url_for('booking', id=id))

        return redirect(url_for('booking', id=id))
        


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
