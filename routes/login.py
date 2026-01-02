from flask import Blueprint, render_template, request, redirect, url_for, session

login_bp = Blueprint("login", __name__)
logout_bp = Blueprint("logout", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        # QUI: verifica credenziali (DB)
        # esempio:
        user_id = 1
        username = 2

        # salva sessione
        session['user_id'] = user_id
        session['username'] = username

        return redirect(url_for('index'))

    return render_template("login.html")

@logout_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))