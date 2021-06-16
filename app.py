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
from flask_paginate import Pagination, get_page_args
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


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if email exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        print(existing_user["_id"])

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                print(existing_user["_id"])
                session["name"] = existing_user["name"]
                session["email"] = existing_user["email"]
                session["user"] = str(existing_user["_id"])
                session["access"] = existing_user["access"]
                flash("Welcome " + session['name'])
                return redirect(url_for("dashboard"))
            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # Email doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return redirect(url_for("login"))


@app.route("/signout")
def signout():
    # remove email from session cookie
    session.pop("email")
    session.pop("user")
    session.pop("name")
    session.pop("access")
    return redirect(url_for("login"))



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
        if booking["status"] == "completed":
            completed_percentage += 1
            total_sales += int(booking["value"])
        elif booking["status"] == "no-show":
            no_show_percentage += 1

    if avg_booking_value == 0:
        avg_booking_value = 0
    else:
        avg_booking_value = int(total_sales / completed_percentage)

    total_sales = int(total_sales)

    if completed_percentage == 0:
        completed_percentage = 0
    else:
        completed_percentage = int((completed_percentage / total_bookings) * 100)

    if no_show_percentage == 0:
        no_show_percentage = 0
    else:
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
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 5

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
    total = len(team)
    pagination_team = get_pagination(data=team, page=page, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)  

    return render_template("team.html", 
                            admin=admin, 
                            team=pagination_team,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            title=title)


@app.route("/user/<id>")
def user(id):
    title = "Team"
    user = mongo.db.users.find_one(
            {"_id": ObjectId(id)})
    print(user)
    return render_template("team-detail.html", title=title, user=user)


@app.route("/update_user/<id>", methods=["GET", "POST"])
def update_user(id):
    if request.form.get("password"):
        mongo.db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.form.get("name"),
                "email": request.form.get("email"),
                "access": request.form.get("access"),
                "position": request.form.get("position"),
                "password": request.form.get("password")
                }
            }
        )
    else:
        mongo.db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.form.get("name"),
                "email": request.form.get("email"),
                "access": request.form.get("access"),
                "position": request.form.get("position")
                }
            }
        )
        
    flash("User Updated Successfully")
    return user(id)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    title = "Add Team Member"
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("User, " + existing_user["name"] + ", already has this email address")
            return render_template("team-add.html", title=title)

        else:
            user = {
                "name": request.form.get("name"),
                "email": request.form.get("email").lower(),
                "position": request.form.get("position"),
                "access": request.form.get("access"),
                "password": generate_password_hash(request.form.get("password")),
                "created_by": session["email"],
                "created_date": datetime.today(),
                "updated_by": session["email"],
                "updated_date": datetime.today()
            }
            _id = mongo.db.users.insert_one(user).inserted_id

            flash("User Added")
            return redirect(url_for('user', id=_id))
    else:
        return render_template("team-add.html", title=title)


@app.route("/delete_user/<id>", methods=["GET", "POST"])
def delete_user(id):
    mongo.db.users.remove({"_id": ObjectId(id)})
    flash("User Successfully Deleted")
    return redirect(url_for('team'))


def get_pagination(data, page, offset=0, per_page=10):
    offset = ((page - 1) * per_page)
    return data[offset: offset + per_page]


@app.route("/guests")
def guests():
    title = "Guests"
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 5

    guests = list(mongo.db.clients.find())
    for x in range(len(guests)):
        guests[x]["rating"] = int(guests[x]["rating"])

    total = len(guests)
    pagination_guests = get_pagination(data=guests, page=page, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)  

    return render_template('guests.html',
                           guests=pagination_guests,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           title=title
                        )


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

    total_bookings = len(bookings)
    total_sales = 0
    no_show_percentage = 0
    completed_percentage = 0
    avg_booking_value = 0
    for booking in bookings:
        if booking["status"] == "completed":
            completed_percentage += 1
            total_sales += int(booking["value"])
        elif booking["status"] == "no-show":
            no_show_percentage += 1

    if total_sales == 0:
        avg_booking_value = 0
    else:
        avg_booking_value = int(total_sales / completed_percentage)

    total_sales = int(total_sales)

    if completed_percentage == 0:
        completed_percentage = 0
    else:
        completed_percentage = int((completed_percentage / total_bookings) * 100)

    if no_show_percentage == 0:
        no_show_percentage = 0
    else:
        no_show_percentage = int((no_show_percentage / total_bookings) * 100)

    guest_age = (datetime.now() - guest["created_date"]).days
    # Calculating years
    years = guest_age // 365

    # Calculating months
    months = (guest_age - years *365) // 30

    # Calculating days
    days = (guest_age - years * 365 - months*30)

    guest_age = str(years) + "Y " + str(months) + "M " + str(days) + "D"

    stats = {
        "guest_age": guest_age,
        "total_bookings": total_bookings,
        "total_sales": total_sales,
        "no_show_percentage": no_show_percentage,
        "completed_percentage": completed_percentage,
        "avg_booking_value": avg_booking_value
    }
    return render_template("guest-detail.html", guest=guest, bookings=bookings, stats=stats, title=title)


@app.route("/update_guest/<id>", methods=["GET", "POST"])
def update_guest(id):
    if request.method == "POST":
        guest = mongo.db.clients.find_one(
            {"_id": ObjectId(id)})

        if request.form.get("notes_service"):
            mongo.db.clients.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "notes_service": request.form.get("notes_service"),
                    "notes_kitchen": request.form.get("notes_kitchen"),
                    "notes_allergies": request.form.get("notes_allergies")
                    }
                }
            )
            flash("Guest Notes for " + guest["first_name"] + " " + guest["last_name"] + " Updated Successfully")
        else:
            marketing_consent = "on" if request.form.get("marketingConsent") else "off"
            dob = datetime.strptime(request.form.get("dob"), '%Y-%m-%d') if request.form.get("dob") else ""
            mongo.db.clients.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "first_name": request.form.get("first_name"),
                    "last_name": request.form.get("last_name"),
                    "email_address": request.form.get("email_address"),
                    "mobile": request.form.get("mobile"),
                    "dob": dob,
                    "rating": request.form.get("rating"),
                    "marketing_consent": marketing_consent,
                    "updated_by": "sreninc@gmail.com",
                    "updated_date": datetime.today()
                    }
                }
            )
            flash("Booking Details for " + guest["first_name"] + " " + guest["last_name"] + "Updated Successfully")
            
            return redirect(url_for('guest', id=id))

        return redirect(url_for('guest', id=id))


@app.route("/add_guest", methods=["GET", "POST"])
def add_guest():
    title = "Add Guest"
    if request.method == "POST":
        existing_user = mongo.db.clients.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Guest, " + existing_user["first_name"] + " " + existing_user["last_name"] + ", already has this email address")
            return render_template("guest-add.html", title=title)

        else:
            marketing_consent = "on" if request.form.get("marketingConsent") else "off"
            dob = datetime.strptime(request.form.get("dob"), '%Y-%m-%d') if request.form.get("dob") else ""
            client = {
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "email": request.form.get("email").lower(),
                "mobile": request.form.get("mobile"),
                "marketing_consent": marketing_consent,
                "rating": request.form.get("rating"),
                "dob": dob,
                "bookings": 0,
                "bookings_completed": 0,
                "value": 0,
                "notes_service": "",
                "notes_kitchen": "",
                "notes_allergies": "",
                "created_by": session["email"],
                "created_date": datetime.today(),
                "updated_by": session["email"],
                "updated_date": datetime.today()
            }
            _id = mongo.db.clients.insert_one(client).inserted_id

            flash("Guest Added")
            return redirect(url_for('guest', id=_id))
    else:
        return render_template("guest-add.html", title=title)


@app.route("/delete_guest/<id>", methods=["GET", "POST"])
def delete_guest(id):
    mongo.db.clients.remove({"_id": ObjectId(id)})
    flash("Guest Successfully Deleted")
    return redirect(url_for('guests'))


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
            flash("Guest Notes for " + guest["first_name"] + " " + guest["last_name"] + " Updated Successfully")
        else:
            mongo.db.bookings.update(
                {"_id": ObjectId(id)},
                {"$set": {
                    "date": request.form.get("date"),
                    "time": request.form.get("time"),
                    "people": request.form.get("people"),
                    "status": request.form.get("status"),
                    "value": request.form.get("value"),
                    "rating": request.form.get("rating"),
                    "updated_by": "sreninc@gmail.com",
                    "updated_date": datetime.today()
                    }
                }
            )
            flash("Booking Details for " + guest["first_name"] + " " + guest["last_name"] + "Updated Successfully")
            
            return redirect(url_for('booking', id=id))

        return redirect(url_for('booking', id=id))


@app.route("/add_booking/<id>", methods=["GET", "POST"])
def add_booking(id):
    title = "Add Booking"
    if request.method == "POST":
        booking = {
            "client_id": id,
            "date": request.form.get("date"),
            "time": request.form.get("time"),
            "people": request.form.get("people"),
            "status": request.form.get("status"),
            "value": request.form.get("value"),
            "rating": request.form.get("rating"),
            "created_by": session["email"],
            "created_date": datetime.today(),
            "updated_by": session["email"],
            "updated_date": datetime.today()
        }
        _id = mongo.db.bookings.insert_one(booking).inserted_id

        flash("Booking Added")
        return redirect(url_for('booking', id=_id))
    else:
        guest = mongo.db.clients.find_one(
            {"_id": ObjectId(id)})
        return render_template("booking-add.html", title=title, guest=guest)


@app.route("/delete_booking/<id>", methods=["GET", "POST"])
def delete_booking(id):
    booking = mongo.db.bookings.find_one(
        {"_id": ObjectId(id)})
    date = booking["date"]
    mongo.db.bookings.remove({"_id": ObjectId(id)})
    flash("Booking Successfully Deleted")
    return redirect(url_for('/bookings/date/', date=date, status="all"))


def generate_pagination_query(query, sort=None, next_key=None):
    sort_field = None if sort is None else sort[0]
    print("sort field")
    print(sort_field)

    def next_key_fn(items):
        if len(items) == 0:
            return None
        item = items[-1]
        if sort_field is None:
            return {'_id': item['_id']}
        else:
            return {'_id': item['_id'], sort_field: item[sort_field]}

    if next_key is None:
        return query, next_key_fn

    paginated_query = query.copy()

    if sort is None:
        paginated_query['_id'] = {'$gt': next_key['_id']}
        return paginated_query, next_key_fn

    sort_operator = '$gt' if sort[1] == 1 else '$lt'

    pagination_query = [
        {sort_field: {sort_operator: next_key[sort_field]}},
        {'$and': [
            {sort_field: next_key[sort_field]},
            {'_id': {sort_operator: next_key['_id']}},
        ]},
    ]

    if '$or' not in paginated_query:
        paginated_query['$or'] = pagination_query
    else:
        paginated_query = {'$and': [query, {'$or': pagination_query}]}

    return paginated_query, next_key_fn


@app.route('/query')
def query():
    query = {}
    sort = ['first_name', -1]
    limit = 2
    query, next_key_fn = generate_pagination_query(query, sort)
    guests = list(mongo.db.clients.find(query).limit(limit).sort([sort]))
    next_key = next_key_fn(guests)
    print(guests)
    print(next_key)
    return redirect(url_for('guests'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
