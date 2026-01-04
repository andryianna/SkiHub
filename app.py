from flask import Flask, render_template, request
from sqlalchemy import func
import os

from dbModels.Resort import Resort
from dbModels.db import db
from dotenv import load_dotenv
from routes.profile import profile_bp
from routes.login import login_bp
from routes.register import register_bp


def init():
    app.register_blueprint(profile_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)

load_dotenv()
app = Flask(__name__)
app.secret_key = "key"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

init()
@app.route("/", methods=["GET"])
def index():
    query = Resort.query

    name = request.args.get("name")
    region = request.args.get("region")
    min_altitude = request.args.get("min_altitude")
    min_slopes = request.args.get("min_slopes")
    order = request.args.get("order")

    if name:
        query = query.filter(Resort.name.ilike(f"%{name}%"))

    if region:
        query = query.filter_by(region=region)

    if min_altitude:
        query = query.filter(Resort.altitude_max >= int(min_altitude))

    if min_slopes:
        query = query.outerjoin(Resort.slopes) \
                     .group_by(Resort.id) \
                     .having(func.count() >= int(min_slopes))

    if order == "name":
        query = query.order_by(Resort.name)
    elif order == "altitude":
        query = query.order_by(Resort.altitude_max.desc())

    resorts = query.all()

    return render_template("index.html", resorts=resorts)

if __name__ == "__main__":
    app.run(port=3000, debug=True)

