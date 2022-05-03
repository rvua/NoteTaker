import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.note import Note

# =========================
# Create Note Routes 
# =========================
@app.route("/new_note")
def new_note():
    if "user_id" not in session:
        flash("Please register or login")
        return redirect("/")
    return render_template("new_note.html")

@app.route("/create_note", methods=['POST'])
def create_note():
    #1. Validate info about note
    if not Note.validate_note(request.form):
        return redirect("/new_note")
    #2. Save note to db w/ logged in user's info attached
    data = {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "note" : request.form['note'],
        "user_id" : session['user_id']
    }
    Note.save_note(data)
    #3. Send us where we need to go.
    return redirect("/dashboard") 
