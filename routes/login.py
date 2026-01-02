from flask import Blueprint, render_template, request, redirect, url_for, session

from dbModels.users import User

login_bp = Blueprint("login", __name__)
logout_bp = Blueprint("logout", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        data = request.json

        user = User(data["username"], data["password"])
        query = User.query.filter_by(username=data["username"]).first()
        if query is None:
            error = "User not found"
        passw = User.query.filter_by(username=data["username"]).get(data["password"])
        if passw is None:
            error = "Incorrect password"
    return render_template("login.html")

@logout_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))