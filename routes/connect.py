from flask import Blueprint, jsonify
from sqlalchemy import text
from db import db

connect_bp = Blueprint("connect_bp", __name__)

@connect_bp.route("/connect", methods=["POST"])
def connect():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"success": True, "message": "Connesso a MySQL"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
