from flask import jsonify
from sqlalchemy import text
from db import db

from app import connect

@connect.route("/connect", methods=["POST"])
def connect():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"success": True, "message": "Connesso a MySQL"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
