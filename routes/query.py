from flask import Blueprint, request, jsonify
from sqlalchemy import text
from db import db

query_bp = Blueprint("query_bp", __name__)

@query_bp.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    sql = data.get("sql", "").strip()

    if not sql:
        return jsonify({"error": "Query vuota"}), 400

    # Sicurezza minima: permetti solo SELECT
    if not sql.lower().startswith("select"):
        return jsonify({"error": "Solo query SELECT consentite"}), 403

    try:
        result = db.session.execute(text(sql))
        rows = [dict(row) for row in result]
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
