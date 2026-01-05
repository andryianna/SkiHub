from app import app
# NON RUNNARE A CASO
from dbModels.User import User

from dbModels.db import db

with app.app_context():
    db.drop_all()
    db.create_all()
