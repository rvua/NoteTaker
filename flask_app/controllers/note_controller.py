from flask_app import app
from flask import render_template, redirect, request, session, flash

# =========================
# Create Note Routes 
# =========================
@app.route("/new_note")
def new_note():
    return render_template("new_note.html")
