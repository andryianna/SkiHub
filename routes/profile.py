from flask import session, redirect, url_for, render_template, Blueprint
from dbModels.SavedResort import SavedResort
from dbModels.PurchaseHistory import Purchase
from dbModels.users import User

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    user = User.query.get(session["user_id"])
    purchases = Purchase.query.filter_by(user_id=user.id).all()
    saved_resorts = SavedResort.query.filter_by(user_id=user.id).all()

    return render_template(
        "profile.html",
        user=user,
        purchases=purchases,
        saved_resorts=saved_resorts
    )