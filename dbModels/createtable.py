from app import app
from sqlalchemy import text
# NON RUNNARE A CASO
from dbModels.Resort import Resort
from dbModels.Lift import Lift
from dbModels.Slope import Slope

from dbModels.db import db

with app.app_context():
    db.drop_all()
    db.create_all()
