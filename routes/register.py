from flask import Blueprint, request, render_template, jsonify
from dbModels.users import User
from dbModels.db import db
from datetime import datetime

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if not request.is_json:
        print("Content-Type non JSON:", request.content_type)
        return jsonify({"error": "Invalid Content-Type"}), 415

    data = request.get_json()
    print("DATA RECEIVED:", data)

    try:
        user = User(
            username=data["username"],
            first_name=data["firstname"],
            last_name=data["lastname"],
            birth_date=datetime.strptime(
                data["dateOfBirth"], "%Y-%m-%d"
            ).date(),
            email=data["email"],
            password=data["password"]
        )

        db.session.add(user)
        db.session.commit()

        print("USER CREATED:", user.username)
        return jsonify({"success": True}), 200

    except Exception as e:
        db.session.rollback()
        print("REGISTER ERROR:", type(e).__name__, e)
        return jsonify({"success": False, "error": str(e)}), 400
