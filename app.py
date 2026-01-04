from flask import Flask, render_template, request
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
@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    data = request.get_json()
    query = Resort.query
    if data.get('name'):
        query = query.filter(Resort.name == data.get('name'))

    resorts = query.all()

    return [{"id":r.id,
             "name":r.name,
             "region":r.region
             }for r in resorts]



if __name__ == "__main__":
    app.run(port=3000, debug=True)

