from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.note import Note
# =========================
# Create Note Routes 
# =========================
@app.route("/new_note")
def new_note():
    return render_template("new_note.html")

@app.route("/create_note")
def create_note():
    #1. Validate info about note
    if not Note.validate_note(request.form):
        return redirect("/new_note")
    #2. Save note to db w/ logged in user's info attached
    #3. Send us where we need to go.
    return redirect("/dashboard") 
