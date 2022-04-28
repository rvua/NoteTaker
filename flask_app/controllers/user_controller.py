import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# 1 =========================
# Render Login/Reg Page 
# ===========================
@app.route("/")
def index():
    return render_template("index.html")

# 2 =========================
# Process Register Route 
# ===========================
@app.route("/register", methods=['POST'])
def register():
    # 1. validate form information
    if not User.validate_register(request.form):
        return redirect("/") 
    # 2. register user == save them to the database
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash,
    }
    user_id = User.save_user(data)
    # 3. Put id into session, effectively logging them in
    session['user_id'] = user_id
    # 4. send them where they need to go. Go to dashboard
    flash("Successful User Registration")
    return redirect("/dashboard")

# 4 =========================
# Process Login Route 
# ===========================
@app.route("/login", methods=['POST'])
def login():
    # 1. validate user before logging in
    if not User.validate_login(request.form):
        return redirect("/")
    # 2. login the validated user / add id to session
    data = {
        "email" : request.form['email']
    }
    logged_user = User.get_by_email(data)
    session['user_id'] = logged_user.id
    # 3. send them where they need to go i.e. the dashboard
    flash("Successful User Login")
    return redirect("/dashboard")

# 3 =========================
# Render Dashboard Route 
# ===========================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please register or login")
        return redirect("/")
    data = {
        "user_id" : session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template("dashboard.html", user = logged_user)

# ==========================
# Logout Route
# ==========================
@app.route("/logout")
def logout():
    session.clear()
    flash("Successfully logged out")
    return redirect("/")