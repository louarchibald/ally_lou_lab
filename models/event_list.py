from models.event import *

event1 = Event("19/05/22", "Coding Conference", "21", "Python Room 101", "Beginners guide to coding.")
event2 = Event("24/05/22", "Start Up 101", "170", "Committee Room No9", "Networking with Tech Professionals.")
event3 = Event("31/05/22", "G31 Graduation", "25", "Zoom Room", "Student end-of-course celebrations.")
events= [event1, event2, event3]

def add_new_event(event):
    events.append(event)