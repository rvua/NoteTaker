from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# =========================
# Render Login/Reg Page 
# =========================
@app.route("/")
def index():
    return render_template("index.html")
