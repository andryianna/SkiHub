from flask import Blueprint, render_template, request, redirect, url_for, session

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # salva utente nel DB

        # login automatico dopo registrazione (best practice)
        session['user_id'] = 1
        session['username'] = 2

        return redirect(url_for('index'))

    return render_template("register.html")