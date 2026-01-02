from flask import session, redirect, url_for, render_template, Blueprint

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login.login'))
    return render_template("profile.html")