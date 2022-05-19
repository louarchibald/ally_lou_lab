from app import app
from flask import render_template, request
from models.event_list import events, add_new_event
from models.event import Event

@app.route("/events")
def event_list():
    return render_template("index.html", title="Event Planner", events=events)

@app.route("/events", methods=["POST"])
def add_event():
    event_name = request.form["event-name"]
    event_date = request.form["event-date"]
    num_of_guests = request.form["num_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    new_event = Event(event_date, event_name, num_of_guests,room_location, description)
    add_new_event(new_event)

    return render_template("index.html", title="Event Planner", events=events)
